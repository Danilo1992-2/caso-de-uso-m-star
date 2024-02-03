from marshmallow import Schema, fields

class ProductSchema(Schema):
    id: int = fields.Integer()
    product_name: str = fields.Str(required=True)
    product_code: str = fields.Str(required=True)
    product_type: str = fields.Str(required=True)
    product_manufacturer: str = fields.Str(required=True)
    description: str = fields.Str(required=True)
    user_id: int = fields.Integer()
