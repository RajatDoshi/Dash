import time
import numpy as np
import copy

import easypost
easypost.api_key = 'EZTK21fb019004dc4e16883b0e3931a890fbHKlpAlwhJVFj9xKF3ES3qA'
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDZ4CKmUWDamVjSONXT4zEV6Rhj0roFdDU')

class Option:
    def __init__(self, product, seller, price, address, distance):
        self.product = product
        self.seller = seller
        self.price = price
        self.address = address
        self.distance = distance
        self.rate = None
        self.delivery = None
        self.service = None
        self.score = None

    def set_shipping(self, rate, delivery, service):
        self.rate = rate
        self.delivery = delivery
        self.service = service

    def set_score(self, score):
        self.score = score

def get_shipping_options(buyer, items, check_n=3):
    shipping_options = []

    from_address_list = [f'{it.street}, {it.city}, ' \
        f'{it.state}, {it.zip}, {it.country}' for it in items]

    if buyer:
        to_address = f'{buyer.street}, {buyer.city}, ' \
            f'{buyer.state}, {buyer.zip}, {buyer.country}'
        distances = get_distance(from_address_list, to_address)
    else:
        distances = [None for _ in items]

    for it, from_address, dist in zip(items, from_address_list, distances):
        option = Option(it.product, it.seller, it.price, from_address, dist)
        shipping_options.append(option)

    if buyer:
        sorted_options = [shipping_options[i] for i in np.argsort(distances)]

        deep_estimates = []
        scores = []
        for i in range(check_n):
            for rate in get_shipment(sorted_options[i].address, to_address):
                estimate = copy.copy(sorted_options[i])
                estimate.set_shipping(
                    rate['cost'],
                    rate['delivery'],
                    rate['service'])
                score = score_function(rate['cost'], rate['delivery'])
                estimate.set_score(score)
                deep_estimates.append(estimate)
                scores.append(score)

        print(scores)
        deep_estimates = [deep_estimates[i] for i in np.argsort(scores)]
        sorted_options = deep_estimates + sorted_options[check_n:]
    else:
        sorted_options = shipping_options

    return sorted_options

def get_distance(from_address_list, to_address):
    # We assign to_address as origin and from_address as destination for convenience
    # Assume distance is same to and from
    # Return: list of distances in km
    output = gmaps.distance_matrix(to_address, from_address_list)\
        ['rows'][0]['elements']
    distances = [x['distance']['value'] / 1000. for x in output]
    return distances

def get_shipment(from_address, to_address):
    """
    Get shipping rate and delivery time estimates
    Warning: SLOW (about 1s)
    """
    from_address = from_address.split(', ')
    from_address = easypost.Address.create(
        verify_strict=['delivery'],
        street1=from_address[0],
        city=from_address[1],
        state=from_address[2],
        zip=from_address[3],
        country=from_address[4],
    )

    to_address = to_address.split(', ')
    to_address = easypost.Address.create(
        verify_strict=['delivery'],
        street1=to_address[0],
        city=to_address[1],
        state=to_address[2],
        zip=to_address[3],
        country=to_address[4],
    )

    parcel = easypost.Parcel.create(
        length=10,
        width=10,
        height=10,
        weight=10
    )

    shipment = easypost.Shipment.create(
        to_address=to_address,
        from_address=from_address,
        parcel=parcel,
    )

    rates = []
    for rate in shipment['rates']:
        rates.append({
            'carrier' : rate['carrier'],
            'currency' : rate['currency'],
            'cost' : float(rate['rate']),
            'delivery' : float(rate['delivery_days']) \
                if rate['delivery_days'] else None,
            'service' : rate['service']
        })
    return rates

def score_function(rate, delivery):
    if rate is None or delivery is None:
        return np.inf
    return np.round((rate**0.6)* (delivery**0.4), decimals=2)
