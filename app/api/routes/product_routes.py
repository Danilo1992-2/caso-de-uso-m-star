from flask import jsonify, request
from config import SessionLocal
from model.product import Product
from schemas.product_schema import ProductSchema
from services.product_services import add_product
from services.product_services import get_product_by_code
from services.product_services import get_all_product
from services.product_services import remove_product

def create_product() -> str:
    data: Product = request.get_json()
    product_schema = ProductSchema()
    errors = product_schema.validate(data)

    if errors:
        return jsonify({'errors': errors}), 400
    
    product_data: dict = product_schema.load(data)
    result: str = add_product(SessionLocal(), product_data)
    return jsonify({"Response": result})


def product_by_code(product_code: int) -> dict:
    result: Product = get_product_by_code(SessionLocal(), product_code=product_code)
    
    if result == None:
        return jsonify({"Response": "Nenhum produto encontrado, verifique o código."}), 200
    
    product_schema = ProductSchema()
    data: dict = product_schema.dump(result)
    return jsonify({"Response": data}), 200


def get_all_products() -> 'list[dict]':
    result: 'list[Product]' = get_all_product(SessionLocal())
    product_schema = ProductSchema(many=True)
    products_data: 'list[dict]' = product_schema.dump(result)
    return jsonify({"Response": products_data}), 200


def delete_product(product_code: int) -> str:
    result = get_product_by_code(SessionLocal() ,product_code)
    delete = remove_product(SessionLocal(), result)
    
    return jsonify({"Response": f"{delete}"})
