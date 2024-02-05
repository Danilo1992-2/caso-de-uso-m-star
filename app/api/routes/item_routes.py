from flask import jsonify, request
from config import SessionLocal
from model.item import EntryItem
from model.item import OutputItem
from model.product import Product
from schemas.item_schema import itemSchema
from services.item_services import entry_item as entry
from services.item_services import output_item as output
from services.product_services import get_product_by_id
from services.item_services import get_all_entry_item
from services.item_services import get_all_output_item

def entry_item() -> str:
    data: EntryItem = request.get_json()
    
    product: Product = get_product_by_id(SessionLocal(),data['product_id']) 
    
    if (product == None):
        return jsonify({"error": "Produto não encontrado"}), 404

    item_schema = itemSchema()
    errors = item_schema.validate(data)

    if errors:
        return jsonify({"error": errors}), 400
    
    item_data: dict = item_schema.load(data)
    result: str = entry(SessionLocal(), item_data)
    
    return jsonify({"Response": result}), 200

def output_item() -> str:
    data: OutputItem = request.get_json()
    
    product: Product = get_product_by_id(SessionLocal(), data['product_id']) 
    
    if (product == None):
        return jsonify({"error": "Produto não encontrado"}), 404

    item_schema = itemSchema()
    errors = item_schema.validate(data)
    
    if errors:
        return jsonify({"error": errors}), 400
    
    item_data: dict = item_schema.load(data)
    result: str = output(SessionLocal(), item_data)
    
    return jsonify({"Response": result}), 200


def get_entry() -> dict:
    data = get_all_entry_item(SessionLocal())
    
    if data == None:
        return jsonify({"Return": data}), 404
    
    return jsonify({"Response": data}), 200

def get_output() -> dict:
    data = get_all_output_item(SessionLocal())
    
    if data == None:
        return jsonify({"Return": data}), 404

    return jsonify({"Response": data}), 200
