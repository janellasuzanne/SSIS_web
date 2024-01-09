from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class AddCollegeForm(FlaskForm):
    collegeCodeInput = StringField('College Code', validators=[
        validators.DataRequired(),
        validators.Regexp(regex=r'^[a-zA-Z]+$', message='College Code should only contain upper or lower case letters.')])
    collegeNameInput = StringField('College Name', validators=[
        validators.DataRequired(),
        validators.Regexp(regex=r'^[a-zA-Z\s]+$', message='College Name should only contain upper or lower case letters and spaces.')
    ])
    submitCollege = SubmitField('Add College')