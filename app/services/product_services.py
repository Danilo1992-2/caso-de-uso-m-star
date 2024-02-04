from model.product import Product
from sqlalchemy.orm import sessionmaker
from datetime import datetime


def add_product(db: sessionmaker, new_product_data: Product) -> str:
    new_product = Product()
    new_product.product_name = new_product_data['product_name']
    new_product.product_code = new_product_data['product_code']
    new_product.product_manufacturer = new_product_data['product_manufacturer']
    new_product.product_type = new_product_data['product_type']
    new_product.description = new_product_data['description']
    new_product.user_id = new_product_data['user_id']
    new_product.createat = datetime.now()
    db.add(new_product)
    db.commit()
    db.close_all()
    return f"{new_product.product_name} - registrado"

def remove_product(db: sessionmaker, product_data: Product) -> str:
    db.delete(product_data)
    db.commit()
    db.close_all()
    
    return f"{product_data.product_name} - Removido"

def get_product_by_code(db: sessionmaker, product_code: str) -> Product:
    data = db.query(Product).filter(Product.product_code == product_code).first()
    db.close_all()
    return data

def get_all_product(db: sessionmaker) -> 'list[Product]':
    data = db.query(Product).all()
    db.close_all()
    return data
