import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/flask_todo'
db = SQLAlchemy(app)


@app.route('/')
def home():
    """Print 'Hello, world!' as the response body."""
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/users/data', methods=['POST'])
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
