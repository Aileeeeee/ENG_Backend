from marshmallow import Schema, fields, validate, validates, ValidationError


class RegisterSchema(Schema):

    email = fields.Email(required=True)
    password = fields.String(
        required=True,
        validate=validate.Length(min=8, max=128)
    )
    first_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=80)
    )
    last_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=80)
    )
    phone = fields.String(validate=validate.Length(max=20))

    @validates("password")
    def validate_password(self, value):
        if not any(c.isupper() for c in value):
            raise ValidationError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValidationError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            raise ValidationError("Password must contain at least one number")


class LoginSchema(Schema):
    """Validates login credentials."""

    email = fields.Email(required=True)
    password = fields.String(required=True)


class UpdateProfileSchema(Schema):
    """Validates profile update. All fields optional."""

    first_name = fields.String(validate=validate.Length(min=1, max=80))
    last_name = fields.String(validate=validate.Length(min=1, max=80))
    phone = fields.String(validate=validate.Length(max=20))
    address = fields.String(validate=validate.Length(max=500))


class ChangePasswordSchema(Schema):
    """Validates password change request."""

    current_password = fields.String(required=True)
    new_password = fields.String(
        required=True,
        validate=validate.Length(min=8, max=128)
    )

    @validates("new_password")
    def validate_new_password(self, value):
        if not any(c.isupper() for c in value):
            raise ValidationError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValidationError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            raise ValidationError("Password must contain at least one number")