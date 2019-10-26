from wtforms import Form, StringField, SelectField

class MusicSearchForm(Form):
    choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')

class AlbumForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    artist = StringField('Artist')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)

class UserForm(Form):
    user_types = [('Buyer', 'Buyer'),
                ('Seller', 'Seller'),
                ]
    name = StringField('Name')
    street = StringField('Street')
    city = StringField('City')
    state = StringField('State')
    country = StringField('Country')
    user_type = SelectField('User Type', choices=user_types)
