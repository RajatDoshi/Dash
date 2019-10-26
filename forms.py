from wtforms import Form, StringField, SelectField

class MusicSearchForm(Form):
    choices = [('User', 'User'),
               ('Album', 'Album'),
               ('Publisher', 'Publisher')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')

class AlbumForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    user = StringField('User')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
