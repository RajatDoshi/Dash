from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
