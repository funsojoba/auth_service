from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(request=True)
    email = fields.Str(request=True)
    password = fields.Str(required=True)


class UsernameSchema(Schemax):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
