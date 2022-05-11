from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions 
from flask_sqlalchemy import SQLAlchemy

from controllers import users 

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, Saravanabhan!</p>"

@app.route('/api/users', methods = ['GET', 'POST'])
def users_handlers():
    fns = {
        'GET': users.index, 
        'POST': users.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/users/<username>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def users_handler(username):
    fns = {
        'GET': users.show,
        'PATCH': users.update,
        'PUT': users.update,
        'DELETE': users.destroy
    }
    resp, code = fns[request.method](request, username)
    print(resp)
    return jsonify(resp), code  #DELETE ROUTE IS BUGGY, IT IS NOT RETURNING A RESPONSE. 

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Opps... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": f"{err}.It's not you, it is us"}), 500

if __name__ == '__main__': 
    app.run(debug = True)