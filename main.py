import json
from flask import Flask, render_template, request
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from .models import Buyer

app = Flask(__name__)

DATABASE_URL = 'postgres://localhost:5432/flask_todo'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

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


@app.route('/', methods=['GET', 'POST'])
def home():
    """Print 'Hello, world!' as the response body."""
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

if __name__ == '__main__':
    app.run(debug=True)