from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField, PasswordField
from wtforms.validators import Length, InputRequired, ValidationError,NumberRange

class LoginForm(FlaskForm):
    IdentificationKey = StringField("Identification Key",
            validators=[InputRequired()], render_kw={"placeholder": "Email"})
    Password = PasswordField("Password",
            validators=[InputRequired()], render_kw={"placeholder": "Password"})
    
    submit = SubmitField('Authenticate')
