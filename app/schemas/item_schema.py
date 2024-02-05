from marshmallow import Schema, fields


class itemSchema(Schema):
    id: int = fields.Integer()
    product_id: int = fields.Integer()
