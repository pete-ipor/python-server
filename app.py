from flask import Flask, jsonify, request

app = Flask(__name__)

# Przykładowa baza danych (w pamięci)
items = []

# Endpoint GET - pobieranie wszystkich elementów
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Endpoint POST - dodawanie nowego elementu
@app.route('/api/items', methods=['POST'])
def add_item():
    item = request.get_json()
    items.append(item)
    return jsonify({"message": "Item added", "item": item}), 201

# Endpoint GET - pobieranie konkretnego elementu
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id < len(items):
        return jsonify(items[item_id])
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)