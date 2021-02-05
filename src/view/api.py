from flask import Flask
from flask_restful import Api
from src.resource.product_resource import ProductResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/api/product', endpoint='product')
api.add_resource(ProductResource, '/api/product/<int:id_>', endpoint='products')


@app.route('/')
def index():
    return 'Bem Vindo!'


app.run(debug=True)