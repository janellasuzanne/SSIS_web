from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators

class AddStudentForm(FlaskForm):
    studentIdInput = StringField('ID: xxxx-xxxx', validators=[
        validators.DataRequired(),
        validators.Regexp(regex=r'^\d{4}-\d{4}$', message="ID Should be in (XXXX-XXXX) Format")])
    studentFirstnameInput = StringField('First Name', validators=[
        validators.DataRequired(),
        validators.Regexp(regex=r'^[a-zA-Z\s]+$', message='First Name should only contain upper or lower case letters and spaces.')
    ])
    studentLastnameInput = StringField('Last Name', validators=[
        validators.DataRequired(),
        validators.Regexp(regex=r'^[a-zA-Z\s]+$', message='Last Name should only contain upper or lower case letters and spaces.')
    ])
    studentYearInput = SelectField('Select Year Level', choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year')])
    studentGenderInput = SelectField('Select Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
    studentCourseInput = SelectField('Select Course', choices=[('BSCS', 'Bachelor of Science in Computer Science'), ('BSN', 'Bachelor of Science in Nursing'), ('BSBA', 'Bachelor of Science in Business Administration')])
    submitStudent = SubmitField('Add Student')