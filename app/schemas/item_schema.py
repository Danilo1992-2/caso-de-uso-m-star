from marshmallow import Schema, fields


class itemSchema(Schema):
    id: int = fields.Integer()
    date: str = fields.Str(required=True)
    product_id: int = fields.Integer()
