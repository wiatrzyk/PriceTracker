from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    name = StringField('Item name', validators=[DataRequired()])
    url = StringField('url', validators=[DataRequired()])
    submit = SubmitField('Submit')