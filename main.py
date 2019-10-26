import json
from flask import Flask, render_template, request

from .models import User
from .forms import NewUserForm

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
