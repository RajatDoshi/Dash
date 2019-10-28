from db_creator import User, Product, Item
from forms import UserForm, UserSearchForm, ProductForm, ProductSearchForm, ItemForm, ItemSearchForm
from app import app
from db_setup import init_db, db_session
from shipping import get_shipping_options, get_shipment

from flask import render_template, request, flash, redirect
import numpy as np

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # str(len(db_session.query(Item).all()))

@app.route('/users', methods=['GET', 'POST'])
def user_index():
    form = UserForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User()
        save_user(user, form, new=True)
        return redirect('/users')

    qry = db_session.query(User)
    results = qry.all()

    # table = UserResults(results)
    # table.border = True
    return render_template('users.html', results=results, form=form)

def save_user(user, form, new=True):
    user.name = form.name.data
    user.street = form.street.data
    user.city = form.city.data
    user.state = form.state.data
    user.country = form.country.data
    user.user_type = form.user_type.data

    if new:
        db_session.add(user)

    db_session.commit()

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    item_form = ItemForm(request.form)

    if request.method == 'POST' and item_form.validate():
        product_name = item_form.data['product']
        product = db_session.query(Product).filter(
            Product.name==product_name.lower()).first()

        seller_name = item_form.data['seller']
        seller = db_session.query(User).\
            filter(User.name==seller_name.lower()).\
            filter(User.user_type=='Seller').first()

        if product and seller:
            item = Item()
            save_item(item, item_form, new=True)

            # Add child to Product parent models
            product.items.append(item)
            seller.items.append(item)
            db_session.commit()
        else:
            if not product:
                flash('No products match "{}"'.format(product_name))
            if not seller:
                flash('No sellers match "{}"'.format(seller_name))

            return redirect('/sell')

        flash('Item created successfully!')
        return redirect('/sell')

    product_results = db_session.query(Product).all()
    # product_table = ProductResults(product_results)
    # product_table.border = True

    item_results = join_item_seller(db_session).all()
    # item_table = ItemResults(item_results)
    # item_table.border = True

    return render_template('sell.html',
        product_results=product_results,
        item_results=item_results,
        item_form=item_form)

@app.route('/sell/new_product', methods=['GET', 'POST'])
def new_product():
    """
    Add a new product
    """
    form = ProductForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        product = Product()
        save_product(product, form, new=True)
        flash('Product created successfully!')
        return redirect('/sell')

    return render_template('new_product.html', form=form)

def save_product(product, form, new=True):
    product.name = form.name.data.lower()
    product.category = form.category.data.lower()
    product.width = form.width.data
    product.height = form.height.data
    product.length = form.length.data
    product.weight = form.weight.data

    if new:
        db_session.add(product)

    db_session.commit()

def save_item(item, form, new=True):
    item.product = form.product.data
    item.seller = form.seller.data
    item.price = form.price.data
    item.quantity = True

    if new:
        db_session.add(item)

    db_session.commit()

@app.route('/buy', methods=['GET', 'POST'])
def buy(top_n=20):
    search = ItemSearchForm(request.form)

    if request.method == 'POST':
        results = []
        search_string = search.data['search']

        if search_string:
            qry = join_item_seller(db_session).filter(
                    Item.product.contains(search_string))
            all_results = qry.all()
            results = get_top_items_by_price(all_results, top_n=top_n)
        else:
            results = all_results = join_item_seller(db_session).all()

        if not results:
            flash('No items found!')
            return redirect('/buy')
    else:
        results = all_results = join_item_seller(db_session).all()

    # table = ItemResults(results)
    # table.border = True

    return render_template('buy.html', items=results, form=search,
        top_results=len(results), total_results=len(all_results))

def join_item_seller(db_session):
    return db_session.query(Item).\
        join(User, User.id==Item.seller_id).\
        with_entities(Item.id, Item.product,
            Item.seller, Item.price, Item.quantity,
            User.street.label('street'), User.city.label('city'),
            User.state.label('state'), User.zip.label('zip'),
            User.country.label('country'))

def get_top_items_by_price(results, top_n=20):
    prices = [it.price for it in results]
    sorted_results = [results[i] for i in np.argsort(prices)]
    return sorted_results[:top_n]

@app.route('/buy/<int:id>', methods=['GET', 'POST'])
def optimize(id):
    search = UserSearchForm(request.form)
    # item = db_session.query(Item).get(id)
    item = join_item_seller(db_session).filter(Item.id==id).first()

    if request.method == 'POST':
        buyer_name = search.data['search']
        buyer = db_session.query(User).\
            filter(User.name==buyer_name.lower()).\
            filter(User.user_type=='Buyer').first()

        if buyer:
            baseline_rates = get_shipment(
                from_address=f'{item.street}, {item.city}, ' \
                    f'{item.state}, {item.zip}, {item.country}',
                to_address=f'{buyer.street}, {buyer.city}, ' \
                    f'{buyer.state}, {buyer.zip}, {buyer.country}')

            similar_items = join_item_seller(db_session).filter(
                    Item.product.contains(item.product)).all()
            results = get_shipping_options(buyer=buyer, items=similar_items)
        else:
            flash('Invalid buyer! Please register before placing any orders!')
            return redirect(f'/buy/{id}')
    else:
        baseline_rates = []
        similar_items = join_item_seller(db_session).filter(
                Item.product.contains(item.product))
        results = get_shipping_options(buyer=None, items=similar_items)

    return render_template('optimize.html',
        results=results,
        form=search,
        baseline_rates=baseline_rates)

if __name__ == '__main__':
    app.run(debug=True)
