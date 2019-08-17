from flask import *
from PIL import Image

app = Flask(__name__)


@app.route('/hack')
def hello_world():
    return 'hackerman'


@app.route("/game")
def game():
    try:
        return send_file("Card_Images/2C.png")
    except:
        abort(404)


@app.route('/')
def index():
    user = {'username': 'Miguel','bin':'huh'}
    return '''
<html>
    <head>
        <title>Web App</title>
    </head>
    <body>
        <h1>Hello, ''' + user['bin'] + '''!</h1>
        <h2>HTML Image</h2>
        <img src="http://localhost:5000/game" alt="Trulli">
    </body>
</html>'''
