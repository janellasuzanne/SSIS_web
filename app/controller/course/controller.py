import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for, flash

from . import course
from app.models.courseModel import CourseModel
from app.models.collegeModel import CollegeModel
from app.controller.course.forms import AddCourseForm

@course.route('/course', methods=['GET', 'POST'], endpoint='course')
def course_view():
    add_form = AddCourseForm()
    add_form.collegeIdInput.choices = CollegeModel.get_college_codes()

    if request.method == 'POST':
        if add_form.validate_on_submit():
            collegeId = add_form.collegeIdInput.data
            courseCode = add_form.courseCodeInput.data
            courseName = add_form.courseNameInput.data

            result = CourseModel.add_course(collegeId, courseCode, courseName)
            flash(result)

            return redirect(url_for('course.course'))

    courses = CourseModel.get_courses()
    return render_template("course.html", add_form=add_form, courses=courses)

@course.route('/update_course', methods=['GET', 'POST'])
def update_course():
    if request.method == "POST":
        code = request.form['code']
        name = request.form['name']

        CourseModel.update_course(code, name)
        return redirect(url_for('course.course'))

@course.route('/delete_course', methods=['POST'])
def delete_course():
    if request.method == "POST":
        course_code = request.form['code']
        if course_code:
            result = CourseModel.delete_course(course_code)
            flash(result)
        return redirect(url_for("course.course"))