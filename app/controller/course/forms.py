from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators

class AddCourseForm(FlaskForm):
    # collegeIdInput = SelectField('Select College', choices=[('CCS', 'CCS'), ('CON', 'CON'), ('COET', 'COET')])
    collegeIdInput = SelectField('Select College', choices=[], validators=[validators.DataRequired(message="cannot be empty.")])
    courseCodeInput = StringField('Course Code', validators=[
        validators.DataRequired(message="cannot be empty."),
        validators.Regexp(regex=r'^[a-zA-Z]+$', message='must only contain upper or lower case letters.')])
    courseNameInput = StringField('Course Name', validators=[
        validators.DataRequired(message="cannot be empty."),
        validators.Regexp(regex=r'^[a-zA-Z\s]+$', message='must only contain upper or lower case letters and spaces.')
    ])
    submitCourse = SubmitField('Add Course')