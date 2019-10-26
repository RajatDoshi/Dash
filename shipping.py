import time
from pprint import pprint

import easypost
easypost.api_key = 'EZTK21fb019004dc4e16883b0e3931a890fbHKlpAlwhJVFj9xKF3ES3qA'

class Address(object):
    def __init__(self, street, city, state, zip, country, verify=True,
            address=None):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country

        if address:
            self.address = address
        else:
            if verify:
                try:
                    self.address = easypost.Address.create(
                        verify_strict=['delivery'],
                        street1=street,
                        city=city,
                        state=state,
                        zip=zip,
                        country=country,
                    )
                except easypost.Error as e:
                    raise ValueError(e.http_body)
            else:
                self.address = easypost.Address.create(
                    street1=street,
                    city=city,
                    state=state,
                    zip=zip,
                    country=country,
                )

    @classmethod
    def from_id(cls, id):
        address = easypost.Address.retrieve(id)
        obj = cls(
            address['street1'],
            address['city'],
            address['state'],
            address['zip'],
            address['country'],
            address=address
        )
        return obj

    def get_id(self):
        return self.address['id']

class Parcel(object):
    def __init__(self, length, width, height, weight, parcel=None):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

        if parcel:
            self.parcel = parcel
        else:
            self.parcel = easypost.Parcel.create(
                length=length,
                width=width,
                height=height,
                weight=weight
            )

    @classmethod
    def from_id(cls, id):
        parcel = easypost.Parcel.retrieve(id)
        obj = cls(
            parcel['length'],
            parcel['width'],
            parcel['height'],
            parcel['weight'],
            parcel=parcel
        )
        return obj

    def get_id(self):
        return self.parcel['id']

class Shipment(object):
    def __init__(self, to_address, from_address, parcel, customs_info=None,
            shipment=None):
        self.to_address = to_address
        self.from_address = from_address
        self.parcel = parcel
        self.customs_info = customs_info

        if shipment:
            self.shipment = shipment
        else:
            self.shipment = easypost.Shipment.create(
              to_address=to_address.address,
              from_address=from_address.address,
              parcel=parcel.parcel,
              customs_info=customs_info
            )

    @classmethod
    def from_id(cls, id):
        shipment = easypost.Shipment.retrieve(id)
        to_address = Address.from_id(shipment['to_address']['id'])
        from_address = Address.from_id(shipment['from_address']['id'])
        parcel = Parcel.from_id(shipment['parcel']['id'])

        obj = cls(
            to_address,
            from_address,
            parcel,
            shipment['customs_info'],
            shipment=shipment
        )
        return obj

    def get_id(self):
        return self.shipment['id']

    def get_rates(self, regenerate=False):
        if regenerate:
            self.shipment = self.shipment.get_rates()

        rates = []
        for rate in self.shipment['rates']:
            rates.append({
                'carrier' : rate['carrier'],
                'currency' : rate['currency'],
                'cost' : rate['rate'],
                'delivery' : rate['delivery_days'],
                'service' : rate['service']
            })
        return rates

shipment = Shipment(
    to_address=Address('1415 North Ave', 'Bridgeport', 'CT', '06604', 'US'),
    from_address = Address('15 Prospect Street', 'New Haven', 'CT', '06511', 'US'),
    parcel = Parcel(10, 10, 10, 10)
)
pprint(shipment.get_rates())

# print(shipment.get_id())

# start = time.time()
# shipment = Shipment.from_id('shp_645d40b4718842bc866a91d5f0a9c2b9')
# print(time.time() - start)
# print(shipment.get_rates())
