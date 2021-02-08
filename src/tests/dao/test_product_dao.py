import sys
sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.backend.dao.product_dao import ProductDao
from src.backend.model.product_model import Product
import pytest

@pytest.fixture
def create_product():
    return Product('Short', 20.00, 'muito bonito')

@pytest.fixture
def create_instance():
    return ProductDao()

def test_product_instance(create_instance):
    assert isinstance(create_instance, ProductDao)

def test_product_save(create_product, create_instance):
    prod = create_instance.save(create_product)
    assert prod is not None
    assert isinstance(prod, Product)
    create_instance.delete(prod)

def test_error_not_save(create_instance):
    with pytest.raises(UnmappedInstanceError):
        create_instance.save('Brinquedo')

def test_read_by_id(create_product, create_instance):
    prod = create_instance.save(create_product)
    prod_read = create_instance.read_by_id(prod.id_)
    assert isinstance(prod, Product)
    assert prod_read.name == prod.name
    create_instance.delete(prod)

def test_not_read_by_id(create_instance):
    result = create_instance.read_by_id('texto')
    assert result is None
    

def test_read_all(create_instance):
    prod = create_instance.read_all()
    assert isinstance(prod, list)

def test_not_delete(create_instance):
    with pytest.raises(UnmappedInstanceError):
        create_instance.delete('Deletado')

def test_delete(create_product, create_instance):
    prod = create_instance.save(create_product)
    if prod is None:
        raise Exception('Error to save')
    create_instance.delete(prod)
    result = create_instance.read_by_id(prod.id_)
    assert result is None
    
    
