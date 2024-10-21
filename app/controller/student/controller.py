import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for, flash

from . import student
from app.models.studentModel import StudentModel
from app.models.collegeModel import CollegeModel
from app.models.courseModel import CourseModel
from app.controller.student.forms import AddStudentForm

@student.route('/students', methods=['GET', 'POST'], endpoint='students')
def students():
    add_form = AddStudentForm()
    add_form.studentCollegeInput.choices = CollegeModel.get_college_codes()
    # add_form.studentCourseInput.choices = CourseModel.get_courses_by_college("College of Computer Studies")
    # add_form.studentCourseInput.choice = courseChoices

    if request.method == 'POST':
        if add_form.validate_on_submit():
            studentId = add_form.studentIdInput.data
            studentFirstname = add_form.studentFirstnameInput.data
            studentLastname = add_form.studentLastnameInput.data
            studentCourse = add_form.studentCourseInput.data
            studentYear = add_form.studentYearInput.data
            studentGender = add_form.studentGenderInput.data

            result = StudentModel.add_student(studentId, studentFirstname, studentLastname, studentCourse, studentYear, studentGender)
            flash(result)

            return redirect(url_for('student.students'))

    students = StudentModel.get_students()
    return render_template("student.html", add_form=add_form, students=students)

@student.route('/delete_student', methods=['POST'])
def delete_student():
    if request.method == "POST":
        student_id = request.form['code']
        if student_id:
            result = StudentModel.delete_student(student_id)
            flash(result)
        return redirect(url_for("student.students"))