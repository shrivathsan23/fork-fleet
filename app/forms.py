from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional

# Form for User Registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8)])

    def validate(self, extra_validators = None):
        rv = super().validate(extra_validators)
        if rv:
            if self.password.data != self.confirm_password.data:
                self.confirm_password.errors.append('Passwords must match.')
                return False
        return rv

# Form for User Login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

# Form for placing an order (for customers)
class OrderForm(FlaskForm):
    # List of available menu items, you'd usually fetch this from the database
    menu_item_id = SelectField('Menu Item', coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])

# Form for restaurant creation (for admins)
class RestaurantForm(FlaskForm):
    name = StringField('Restaurant Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=500)])

# Form for adding menu items (for admins)
class MenuItemForm(FlaskForm):
    name = StringField('Dish Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=500)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    restaurant_id = SelectField('Restaurant', coerce=int, validators=[DataRequired()])