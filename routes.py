from app import app
from app.controller import UserController 

@app.route('/users')
# @app.route('/index')
def users():
    return UserController.index()
