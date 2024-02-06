from datetime import datetime

from flask import jsonify, request
import pandas as pd

from config import SessionLocal
from model.product import Product
from model.item import EntryItem
from model.item import OutputItem
from schemas.product_schema import ProductSchema
from schemas.product_schema import ProductItemSchema
from services.product_services import add_product
from services.product_services import get_product_by_code
from services.product_services import get_all_product
from services.product_services import remove_product
from services.product_services import record_csv_db
from services.user_services import get_user_by_id
from services.item_services import get_product_item_exist
from services.item_services import get_all_product_entry
from services.item_services import get_all_product_output


def create_product() -> str:
    data: Product = request.get_json()

    result = get_product_by_code(SessionLocal(), data["product_code"])
    if result != None:
        return jsonify({"Response": "O produto já existe"}), 404

    product_schema = ProductSchema()
    errors = product_schema.validate(data)

    if errors:
        return jsonify({"errors": errors}), 400

    product_data: dict = product_schema.load(data)
    result: str = add_product(SessionLocal(), product_data)
    return jsonify({"Response": result})


def product_by_code(product_code: int) -> dict:
    result: Product = get_product_by_code(SessionLocal(), product_code=product_code)

    if result == None:
        return (
            jsonify({"Response": "Nenhum produto encontrado, verifique o código."}),
            404,
        )

    product_schema = ProductSchema()
    data: dict = product_schema.dump(result)
    return jsonify({"Response": data}), 200


def get_all_products() -> dict:
    result: "list[Product]" = get_all_product(SessionLocal())
    product_schema = ProductSchema(many=True)
    products_data: "list[dict]" = product_schema.dump(result)
    return jsonify({"Response": products_data}), 200


def delete_product(product_code: int) -> str:
    result = get_product_by_code(SessionLocal(), product_code)
    if result == None:
        return jsonify({"Response": "O produto não foi encontrado"}), 404

    item: bool = get_product_item_exist(SessionLocal(), result.id)

    if item:
        return (
            jsonify(
                {
                    "Response": "O Produto não pode ser deletado, há entradas e/ou saídas cadastradas."
                }
            ),
            400,
        )

    delete = remove_product(SessionLocal(), result)

    return jsonify({"Response": f"{delete}"}), 200


def process_csv_file() -> str:
    user_id = request.form.get("user_id")
    if user_id == None:
        return jsonify({"error": "id do usuário não informado"}), 400

    if get_user_by_id(SessionLocal(), user_id) == None:
        return jsonify({"error": "usuário não enconrado"}), 404

    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]
    if not file.filename.endswith(".csv"):
        return jsonify({"error": "O arquivo deve ter extensão CSV"}), 400

    pd.read_csv(file).to_csv("app/files/file.csv")
    record_csv_db(SessionLocal(), user_id)

    return jsonify({"Response": "Arquivo registrado"})


def get_all_product_entry_data() -> dict:
    data = get_all_product_entry(SessionLocal())
    itens: "list[dict]" = []
    date_format = "%d/%m/%Y"

    for item in data:
        values_dict: dict = {
            "product_name": item.Product.product_name,
            "product_code": item.Product.product_code,
            "product_type": item.Product.product_type,
            "product_manufacturer": item.Product.product_manufacturer,
            "description": item.Product.description,
            "status_date": datetime.strftime(item.EntryItem.date, date_format),
            "status": "disponivel" if item.EntryItem.available == 0 else "indisponivel",
        }
        itens.append(values_dict)
    return jsonify({"Response": itens}), 200


def get_all_product_output_data() -> dict:
    data = get_all_product_output(SessionLocal())
    itens: "list[dict]" = []
    date_format = "%d/%m/%Y"

    for item in data:
        values_dict: dict = {
            "product_name": item.Product.product_name,
            "product_code": item.Product.product_code,
            "product_type": item.Product.product_type,
            "product_manufacturer": item.Product.product_manufacturer,
            "description": item.Product.description,
            "status_date": datetime.strftime(item.OutputItem.date, date_format),
            "status": "saida",
        }
        itens.append(values_dict)
    return jsonify({"Response": itens}), 200
