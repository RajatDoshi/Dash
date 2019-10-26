import json
from flask import Flask, render_template, request
<<<<<<< HEAD
=======
from flask import Response
>>>>>>> 7c64612b29f30b3d9ddb7989dbc876c6f03040ae
from flask_sqlalchemy import SQLAlchemy
from .models import Buyer

app = Flask(__name__)

DATABASE_URL = 'postgres://localhost:5432/flask_todo'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

<<<<<<< HEAD
from .models import User
from .forms import NewUserForm
=======
""" Save the changes to the database """
def save_changes(form, new=False):
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    buyer = Buyer()
    buyer.id = form.id.data
    buyer.name = form.name.data
    buyer.location = form.location.data
    if new:
        db.add(buyer)

    # commit the data to the database
    db.commit()
>>>>>>> 7c64612b29f30b3d9ddb7989dbc876c6f03040ae


@app.route('/', methods=['GET', 'POST'])
def home():
    """Print 'Hello, world!' as the response body."""
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

<<<<<<< HEAD
@app.route('/users', methods=['GET', 'POST'])
def buyers():
    form = NewUserForm(request.form)
    if request.method == 'POST':
        create_user(form)

    return render_template('results.html', form=form)

@app.route('/users/results')
def search_results(form):
    results = []
    search_string = form.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Buyer)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/users')
    else:
        # display results
        return render_template('results.html', results=results)
=======
@app.route('/data', methods=['POST'])
def changeModel(data):
    db.session.add(data)
    db.session.commit()
    output = {'msg': 'posted'}
    response = Response(
        mimetype="application/json",
        response=json.dumps(output),
        status=201
    )
    return response
>>>>>>> 7c64612b29f30b3d9ddb7989dbc876c6f03040ae

if __name__ == '__main__':
    app.run(debug=True)