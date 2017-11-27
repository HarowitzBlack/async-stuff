

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey, Index page'

@app.route('/hello')
def hello():
    return 'Hello Hommie'

if __name__ == "__main__":
    app.run(debug=True,port=5000)
