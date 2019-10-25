import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/flask_todo'
db = SQLAlchemy(app)

from .models import User
from .forms import NewUserForm

@app.route('/')
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

if __name__ == '__main__':
    app.run(debug=True)
