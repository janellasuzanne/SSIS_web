import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for, flash

from . import college
from app.models.collegeModel import CollegeModel
from app.controller.college.forms import AddCollegeForm

@college.route('/college', methods=['GET', 'POST'], endpoint='college')
def college_view():
    add_form = AddCollegeForm()

    if request.method == 'POST':
        if add_form.validate_on_submit():
            collegeCode = add_form.collegeCodeInput.data
            collegeName = add_form.collegeNameInput.data

            result = CollegeModel.add_college(collegeCode, collegeName)
            flash(result)

            return redirect(url_for('college.college'))

    colleges = CollegeModel.get_colleges()
    return render_template("college.html", add_form=add_form, colleges=colleges, page_name='colleges')

@college.route('/update_college', methods=['GET','POST'])
def update_college():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        
        CollegeModel.update_college(code, name)
        return redirect(url_for('college.college'))

@college.route('/delete_college', methods=['POST'])
def delete_college():
    if request.method == "POST":
        college_code = request.form['code']
        if college_code:
            result = CollegeModel.delete_college(college_code)
            flash(result)
        return redirect(url_for("college.college"))