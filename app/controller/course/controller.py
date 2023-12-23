import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for

from . import course
from app.models.courseModel import CourseModel

@course.route('/course')
def index():
    courses = CourseModel.get_courses()
    return render_template("course.html", courses=courses)