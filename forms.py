from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, TextAreaField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange
from flask_wtf.file import FileField, FileAllowed

# ---------------------------
# AUTH: LOGIN FORM
# ---------------------------
class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=60)]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=4)]
    )
    submit = SubmitField("Login")


# ---------------------------
# AUTH: REGISTER FORM
# --------------------------- 
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=64)])

    email = StringField("Email", validators=[
        DataRequired(),
        Email(message="Invalid email format.")
    ])

    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Register")



# ---------------------------
# INVENTORY: ADD ITEM FORM
# ---------------------------
class AddItemForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(),
        Length(max=150)
    ])

    description = TextAreaField("Description", validators=[
        Optional(),
        Length(max=500, message="Description cannot exceed 500 characters.")
    ])

    quantity = IntegerField(
        "Quantity",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=100000, message="Quantity must be between 0 and 100,000")
        ]
    )

    price = DecimalField(
        "Price",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=1000000, message="Price must be between 0 and 1,000,000")
        ]
    )

    category = SelectField("Category", choices=[
        ("", "— Choose category —"),
        ("general", "General"),
        ("electronics", "Electronics"),
        ("office", "Office"),
        ("consumable", "Consumable"),
        ("other", "Other")
    ])

    image = FileField("Item Image", validators=[
        FileAllowed(["jpg", "jpeg", "png", "gif"], "Images only!")
    ])

    submit = SubmitField("Save")



# ---------------------------
# INVENTORY: EDIT ITEM FORM
# ---------------------------
class AddItemForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(),
        Length(max=150)
    ])

    description = TextAreaField("Description", validators=[
        Optional(),
        Length(max=500, message="Description cannot exceed 500 characters.")
    ])

    quantity = IntegerField(
        "Quantity",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=100000, message="Quantity must be between 0 and 100,000")
        ]
    )

    price = DecimalField(
        "Price",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=1000000, message="Price must be between 0 and 1,000,000")
        ]
    )

    category = SelectField("Category", choices=[
        ("", "— Choose category —"),
        ("general", "General"),
        ("electronics", "Electronics"),
        ("office", "Office"),
        ("consumable", "Consumable"),
        ("other", "Other")
    ])

    image = FileField("Item Image", validators=[
        FileAllowed(["jpg", "jpeg", "png", "gif"], "Images only!")
    ])

    submit = SubmitField("Save")


class EditProfileForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[Optional(), Email()])
    bio = TextAreaField("Bio", validators=[Optional()])
    phone = StringField("Phone", validators=[Optional(), Length(max=20)])
    location = StringField("Location", validators=[Optional()])
    submit = SubmitField("Save Changes")


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired()])
    submit = SubmitField("Change Password")


class AvatarUploadForm(FlaskForm):
    avatar = FileField("Upload Avatar", validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], "Images only!")
    ])
    submit = SubmitField("Upload")

class AddItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Optional()])
    quantity = IntegerField("Quantity", default=0, validators=[NumberRange(min=0)])
    price = DecimalField("Price", default=0.0, validators=[NumberRange(min=0)])
    category = SelectField("Category", choices=[
        ("", "— Choose category —"),
        ("general", "General"),
        ("electronics", "Electronics"),
        ("office", "Office"),
        ("consumable", "Consumable"),
        ("other", "Other")
    ], default="")
    image = FileField("Item Image", validators=[FileAllowed(["jpg", "jpeg", "png", "gif"], "Images only!")])
    submit = SubmitField("Save")


class EditItemForm(AddItemForm):
    # Inherit fields; templates can change button text
    pass
