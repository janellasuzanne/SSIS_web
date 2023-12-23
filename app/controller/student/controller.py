import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for

from . import student
from app.models.studentModel import StudentModel

@student.route('/student')
def index():
    students = StudentModel.get_students()
    return render_template("student.html", students=students)