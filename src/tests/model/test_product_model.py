import sys
sys.path.append('.')
from src.backend.model.product_model import Product
from src.backend.model.base_model import BaseModel
import pytest


@pytest.mark.parametrize('name, description, price', [
                            ('Blusa', 'florida', 20.90),
                            ('Blusa masculina', '', 100.00)
                        ])
def test_product_instance(name, price, description):
    product = Product(name, price, description)

    assert isinstance(product, Product)
    assert isinstance(product, BaseModel)

@pytest.mark.parametrize('name, description, price', [
                            ('Blusa', 'florida', 20.90),
                            ('Blusa masculina', '', 100.00)
                        ])
def test_product_args(name, price, description):
    product = Product(name, price, description)
    assert product.name == name
    assert product.price == price
    assert product.description == description

@pytest.mark.parametrize('name, description, price', [
                            (10, 'florida', 10.0),
                            ('Blusa masculina', 1.0, 100.00),
                            ('Blusa masculina', 'florida', '100.00')
                        ])
def test_product_return_type_error(name, price, description):
    with pytest.raises(TypeError):
        Product(name, price, description)

@pytest.mark.parametrize('name, description, price', [
                            ('Blusa'*150, 'florida', 10.0),
                            ('', 'florida', 10.0),
                            (' ', 'florida', 10.0),
                            (None, 'florida', 10.0),
                            ('Blusa', 'florida'*300, 10.0),
                            ('Blusa masculina', ' ', -1.0)
                        ])
def test_product_return_value_error(name, price, description):
    with pytest.raises(ValueError):
        Product(name, price, description)


