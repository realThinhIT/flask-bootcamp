from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "Apple Store",
        "items": [
            {
                "name": "MacBook Pro 2019 13\" with Touch Bar",
                "price": 2049.99
            }
        ]
    }
]

# GET / - homepage
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

# GET /store - view available stores
@app.route("/store", methods=["GET"])
def list_stores():
    return jsonify({
        'data': stores
    })

# POST /store - create a store {name}
@app.route("/store", methods=["POST"])
def create_store():
    body = request.get_json()

    new_store = {
        'name': body['name'],
        'items': []
    }
    stores.append(new_store)

    return jsonify(new_store)

# GET /store/<string:name> - retrieve a store with name
@app.route("/store/<string:name>", methods=["GET"])
def get_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify({
                'data': store
            })

    return jsonify({
        'message': "That store doesn't exist ({}).".format(name)
    })

# POST /store/<string:name>/item - create a new item {name, price}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item(name):
    body = request.get_json()

    for store in stores:
        if store.get('name') == name:
            new_item = {
                'name': body['name'],
                'price': body['price']
            }

            store['items'].append(new_item)

            return jsonify({
                'data': new_item
            })

    return jsonify({
        'message': "That store doesn't exist ({}).".format(name)
    })

# GET /store/<string:name>/item - view available items
@app.route("/store/<string:name>/item", methods=["GET"])
def list_items_in_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify({
                'data': store['items']
            })

    return jsonify({
        'message': "That store doesn't exist ({}).".format(name)
    })


app.run(port=3000)
