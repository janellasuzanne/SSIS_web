import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for

from . import college
from app.models.collegeModel import CollegeModel

@college.route('/college')
def index():
    colleges = CollegeModel.get_colleges()
    return render_template("college.html", colleges=colleges)