from flask import Flask, jsonify
from flask_cors import CORS
from product.infrastructure.routers.product_router import producto_router

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(producto_router)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
