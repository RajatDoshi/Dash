from wtforms import Form, StringField, SelectField, FloatField

class UserForm(Form):
    user_types = [('Seller', 'Seller'),
                ('Buyer', 'Buyer')
                ]
    name = StringField('Name')
    street = StringField('Street')
    city = StringField('City')
    state = StringField('State')
    zip = StringField('ZIP')
    country = StringField('Country')
    user_type = SelectField('User Type', choices=user_types)

class UserSearchForm(Form):
    search = StringField('Buyer')

class ProductForm(Form):
    name = StringField('Name')
    category = StringField('Category')
    width = FloatField('Width')
    height = FloatField('Height')
    length = FloatField('Length')
    weight = FloatField('Weight')

class ProductSearchForm(Form):
    search = StringField('Product Name')

class ItemForm(Form):
    product = StringField('Product')
    seller = StringField('Seller')
    price = FloatField('Price')

class ItemSearchForm(Form):
    search = StringField('Product')
