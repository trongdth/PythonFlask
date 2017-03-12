from flask import Flask, jsonify, request, render_template
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.home import Home

app = Flask(__name__, template_folder='../templates')
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'
app.secret_key = 'trongdth'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Home, '/')

# stores = [
#     {
#         'name' : 'My wonderful store',
#         'items' : [
#             {
#                 'name' : 'My Item',
#                 'price' : 15.99
#             }
#         ]
#     }
# ]
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route('/store', methods=["POST"])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         "name" : request_data['name'],
#         "items" : []
#     }
#     stores.append(new_store)
#     return jsonify(new_store)
#
# @app.route("/store/<string:name>", methods=["GET"])
# def get_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify(store)
#
#     return jsonify({ "message" : "store not found"})
#
# @app.route("/store/<string:name>/item", methods=["POST"])
# def create_item_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store['name'] == name:
#             new_item = {
#                 'name' : request_data['name'],
#                 'price' : request_data['price'],
#             }
#             store.append(new_item)
#             return jsonify(new_item)
#     return jsonify ({'message':'store not found'})
#
# @app.route("/store/<string:name>/item")
# def get_item_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify( {'items':store['items'] } )
#     return jsonify ({'message':'store not found'})
#
# @app.route("/store")
# def get_stores():
#     return jsonify({'stores' : stores})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
