from model.item import EntryItem, OutputItem
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from model.item import EntryItem
from model.item import OutputItem
from model.product import Product
from datetime import datetime
import os


def entry_item(db: sessionmaker, new_item_data: EntryItem) -> str:
    new_item = EntryItem()
    new_item.date = datetime.now()
    new_item.product_id = new_item_data["product_id"]

    db.add(new_item)
    db.commit()
    db.close_all()

    return f"{new_item_data['product_id']} - registrado"


def output_item(db: sessionmaker, new_item_data: OutputItem) -> str:
    new_item = OutputItem()
    new_item.date = datetime.now()
    new_item.product_id = new_item_data["product_id"]

    db.add(new_item)
    db.commit()
    db.close_all()

    return f"{new_item_data['product_id']} - registrado"


def get_all_entry_item(db: sessionmaker) -> dict:
    data: list = []
    result = (
        db.query(EntryItem.date, func.count(EntryItem.date).label("product_id"))
        .group_by(EntryItem.date)
        .all()
    )

    for row in result:
        data.append({"Data": f"{row.date}", "Total": f"{row.product_id}"})
    return data


def get_product_item_exist(db: sessionmaker, product_id: int) -> bool:
    entry_data = db.query(EntryItem).filter(EntryItem.product_id == product_id).all()
    output_data = db.query(OutputItem).filter(OutputItem.product_id == product_id).all()

    if len(entry_data) < 1 and len(output_data) < 1:
        return False

    return True


def get_all_output_item(db: sessionmaker) -> dict:
    data: list = []
    result = (
        db.query(OutputItem.date, func.count(OutputItem.date).label("product_id"))
        .group_by(OutputItem.date)
        .all()
    )

    for row in result:
        data.append({"Data": f"{row.date}", "Total": f"{row.product_id}"})
    return data


def get_all_product_output(db: sessionmaker):
    data = (
        db.query(OutputItem, Product)
        .join(Product, OutputItem.product_id == Product.id)
        .all()
    )
    return data


def get_all_product_entry(db: sessionmaker):
    return (
        db.query(EntryItem, Product)
        .join(Product, EntryItem.product_id == Product.id)
        .all()
    )
