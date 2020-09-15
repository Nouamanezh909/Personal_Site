
# import FlaskForm instead od Form to avoid errors
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import (TextField, 
StringField,
 TextAreaField,
  SubmitField, validators)


class ContactForm(FlaskForm):
    name = StringField('Name', 
            [validators.DataRequired()])

    email = EmailField('Email', [validators.DataRequired()])

    subject = TextField("Subject")
    message = TextAreaField("Message",[validators.DataRequired()])
    submit = SubmitField("Send")