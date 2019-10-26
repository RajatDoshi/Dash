from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    user = Col('User')
    title = Col('Title')
    release_date = Col('Release Date')
    publisher = Col('Publisher')
    media_type = Col('Media')
