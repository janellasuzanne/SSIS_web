import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for

from . import student
from app.models.studentModel import StudentModel
from app.controller.student.forms import AddStudentForm

# @student.route('/student')
# def index():
#     students = StudentModel.get_students()
#     return render_template("student.html", students=students)

@student.route('/student', methods=['GET', 'POST'], endpoint='student')
def student():
    add_form = AddStudentForm()

    if request.method == 'POST':
        if add_form.validate_on_submit():
            studentId = add_form.studentIdInput.data
            studentFirstname = add_form.studentFirstnameInput.data
            studentLastname = add_form.studentLastnameInput.data
            studentYear = add_form.studentYearInput.data
            studentGender = add_form.studentGenderInput.data
            studentCourse = add_form.studentCourseInput.data

            StudentModel.add_student(studentId, studentFirstname, studentLastname, studentYear, studentGender, studentCourse)

    students = StudentModel.get_students()
    return render_template("student.html", add_form=add_form, students=students)