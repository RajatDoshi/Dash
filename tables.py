from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    artist = Col('Artist')
    title = Col('Title')
    release_date = Col('Release Date')
    publisher = Col('Publisher')
    media_type = Col('Media')

class UserResults(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    street = Col('Street')
    city = Col('City')
    state = Col('State')
    country = Col('Country')
    user_type = Col('User Type')

class ProductResults(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    category = Col('Category')
    width = Col('Width')
    height = Col('Height')
    length = Col('Length')
    weight = Col('Weight')

class ItemResults(Table):
    id = Col('Id', show=False)
    product = Col('Product')
    seller = Col('Seller')
    price = Col('Price')
    quantity = Col('Quantity')
