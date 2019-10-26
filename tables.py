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
