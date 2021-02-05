from src.backend.dao.base_dao import BaseDao
from src.backend.model.product_model import Product

class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)
