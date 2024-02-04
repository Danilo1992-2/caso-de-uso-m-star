from marshmallow import Schema, fields

class UserSchema(Schema):
    id: int = fields.Int()
    name: str = fields.Str(required=True)
    document: str = fields.Str(required=True)
