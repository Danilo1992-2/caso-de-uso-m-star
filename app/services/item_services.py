from model.item import EntryItem, OutputItem
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from model.item import EntryItem
from model.item import OutputItem
from datetime import datetime
import os


def entry_item(db: sessionmaker, new_item_data: EntryItem) -> str:
    new_item = EntryItem()
    new_item.date = new_item_data['date']
    new_item.product_id = new_item_data['product_id']
    
    db.add(new_item)
    db.commit()
    db.close_all()
    
    return f"{new_item_data['product_id']} - registrado"

def output_item(db: sessionmaker, new_item_data: OutputItem) -> str:
    new_item = OutputItem()
    new_item.date = datetime.now()
    new_item.product_id = new_item_data['product_id']

    db.add(new_item)
    db.commit()
    db.close_all()
    
    return f"{new_item_data['product_id']} - registrado"

def get_all_entry_item(db: sessionmaker) -> dict:
    data: list = []
    result = db.query(
            EntryItem.date,
            func.count(EntryItem.date).label('product_id')
        ).group_by(EntryItem.date).all()
    
    for row in result:
        data.append({'Data': f'{row.date}', 'Total': f'{row.product_id}'})
    return data

def get_all_output_item(db: sessionmaker) -> dict:
    data: list = []
    result = db.query(
            OutputItem.date,
            func.count(OutputItem.date).label('product_id')
        ).group_by(OutputItem.date).all()

    for row in result:
        data.append({'Data': f'{row.date}', 'Total': f'{row.product_id}'})
    return data
