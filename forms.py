from wtforms import Form, StringField, SelectField

class NewUserForm(Form):
    choices = [('name', 'Buyer Name'),
               ('location', 'Location')]
    select = SelectField('Create buyer:', choices=choices)
    search = StringField('')
