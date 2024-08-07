import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for, flash

from . import student
from app.models.studentModel import StudentModel
from app.controller.student.forms import AddStudentForm

@student.route('/students', methods=['GET', 'POST'], endpoint='students')
def students():
    add_form = AddStudentForm()

    if request.method == 'POST':
        if add_form.validate_on_submit():
            studentId = add_form.studentIdInput.data
            studentFirstname = add_form.studentFirstnameInput.data
            studentLastname = add_form.studentLastnameInput.data
            studentYear = add_form.studentYearInput.data
            studentGender = add_form.studentGenderInput.data
            studentCourse = add_form.studentCourseInput.data

            result = StudentModel.add_student(studentId, studentFirstname, studentLastname, studentYear, studentGender, studentCourse)
            flash(result)

            return redirect(url_for('student.students'))

    students = StudentModel.get_students()
    return render_template("student.html", add_form=add_form, students=students)