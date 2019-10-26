from db_creator import Artist, Album, User, Product, Item
from forms import MusicSearchForm, AlbumForm, UserForm, ProductForm, ProductSearchForm, ItemForm, ItemSearchForm
from tables import Results, UserResults, ProductResults, ItemResults
from app import app
from db_setup import init_db, db_session

from flask import render_template, request, flash, redirect

# init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Artist':
            qry = db_session.query(Album, Artist).filter(
                Artist.id==Album.artist_id).filter(
                    Artist.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Album':
            qry = db_session.query(Album).filter(
                Album.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Publisher':
            qry = db_session.query(Album).filter(
                Album.publisher.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Album)
            results = qry.all()
    else:
        qry = db_session.query(Album)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

@app.route('/new_album', methods=['GET', 'POST'])
def new_album():
    """
    Add a new album
    """
    form = AlbumForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        album = Album()
        save_changes(album, form, new=True)
        flash('Album created successfully!')
        return redirect('/')

    return render_template('new_album.html', form=form)

def save_changes(album, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    artist = Artist()
    artist.name = form.artist.data

    album.artist = artist
    album.title = form.title.data
    album.release_date = form.release_date.data
    album.publisher = form.publisher.data
    album.media_type = form.media_type.data

    if new:
        # Add the new album to the database
        db_session.add(album)

    # commit the data to the database
    db_session.commit()

@app.route('/users', methods=['GET', 'POST'])
def user_index():
    form = UserForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User()
        save_user(user, form, new=True)
        return redirect('/users')

    qry = db_session.query(User)
    results = qry.all()

    table = UserResults(results)
    table.border = True
    return render_template('users.html', table=table, form=form)

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
        item = Item()
        save_item(item, item_form, new=True)
        flash('Item created successfully!')
        return redirect('/sell')

    product_results = db_session.query(Product).all()
    product_table = ProductResults(product_results)
    product_table.border = True

    item_results = db_session.query(Item).all()
    item_table = ItemResults(item_results)
    item_table.border = True

    return render_template('sell.html',
        product_table=product_table,
        item_table=item_table,
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
    product.name = form.name.data
    product.category = form.category.data
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
def buy():
    search = ItemSearchForm(request.form)

    if request.method == 'POST':
        results = []
        search_string = search.data['search']

        if search_string:
            qry = db_session.query(Item).filter(
                    Item.product.contains(search_string))
        else:
            qry = db_session.query(Item)

        results = qry.all()

        if not results:
            flash('No items found!')
            return redirect('/buy')
    else:
        results = db_session.query(Item).all()

    table = ItemResults(results)
    table.border = True

    return render_template('buy.html', table=table, form=search)

if __name__ == '__main__':
    app.run(debug=True)
