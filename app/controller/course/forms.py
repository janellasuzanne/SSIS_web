from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators

class AddCourseForm(FlaskForm):
    # collegeIdInput = SelectField('Select College', choices=[('CCS', 'CCS'), ('CON', 'CON'), ('COET', 'COET')])
    collegeIdInput = SelectField('Select College', choices=[])
    courseCodeInput = StringField('Course Code', validators=[
        validators.DataRequired(),
        validators.Regexp(regex=r'^[a-zA-Z]+$', message='College Code should only contain upper or lower case letters.')])
    courseNameInput = StringField('Course Name', validators=[
        validators.DataRequired(),
        validators.Regexp(regex=r'^[a-zA-Z\s]+$', message='College Name should only contain upper or lower case letters and spaces.')
    ])
    submitCourse = SubmitField('Add Course')