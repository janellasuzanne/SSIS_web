import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for

from . import course
from app.models.courseModel import CourseModel
from app.controller.course.forms import AddCourseForm

@course.route('/course', methods=['GET', 'POST'], endpoint='course')
def course():
    add_form = AddCourseForm()

    if request.method == 'POST':
        if add_form.validate_on_submit():
            collegeId = add_form.collegeIdInput.data
            courseCode = add_form.courseCodeInput.data
            courseName = add_form.courseNameInput.data

            CourseModel.add_course(collegeId, courseCode, courseName)

    courses = CourseModel.get_courses()
    return render_template("course.html", add_form=add_form, courses=courses)