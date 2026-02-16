from marshmallow import Schema, fields, validate

class RegisterSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3))
    password = fields.Str(required=True, validate=validate.Length(min=6))
    role = fields.Str(
        validate=validate.OneOf(["user", "admin"]),
        load_default="user"  
    )

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class PostSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)

