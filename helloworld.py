from bottle import get, post, request, route # or route
from bottle import Bottle, run
import sqlite3

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"


@app.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

from bottle import static_file
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=r'C:\Users\jason\OneDrive\Documents\GitHub\test-bottle')

from bottle import error
@app.error(404)
def error404(error):
    return 'ERROR 404 is now replaced with this: Poop'

run(app, host='localhost', port=8080)