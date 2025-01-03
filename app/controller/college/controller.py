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
            if "successfully" in result:
                flash(result, 'success')
            elif "duplicate" in result.lower():
                flash("College not created: Cannot have duplicate colleges.", 'danger')
            else:
                flash(result, 'danger')
            # flash(result, 'success')

            return redirect(url_for('college.college'))
        else:
             for field, errors in add_form.errors.items():
                for error in errors:
                    flash(f"College not created: {field.replace('Input', '').capitalize()} - {error}", 'danger')
            # flash('College NOT created!', 'danger')

    colleges = CollegeModel.get_colleges()
    return render_template("college.html", add_form=add_form, colleges=colleges, page_name='colleges')

@college.route('/update_college', methods=['GET','POST'])
def update_college():
    if request.method == 'POST':
        newCode = request.form.get('code')
        name = request.form.get('name')
        oldCode = request.form.get('hiddenCode')
        
        result = CollegeModel.update_college(newCode, name, oldCode)

        if "successfully" in result:
            flash(result, 'success')
        else:
            flash(result, 'danger')
        # flash(result, 'success')

    return redirect(url_for('college.college'))
    # else:
    #     flash('College information NOT updated!', 'danger')

@college.route('/delete_college', methods=['POST'])
def delete_college():
    if request.method == "POST":
        college_code = request.form['code']
        if college_code:
            result = CollegeModel.delete_college(college_code)
            flash(result, 'success')

        return redirect(url_for("college.college"))
    else:
        flash('College NOT deleted!', 'danger')
    
    
@college.route('/search_college', methods=['GET', 'POST'])
def search_college():
    add_form = AddCollegeForm()

    filter_option = request.form.get('filter')
    search_input = request.form.get('search_input')

    if not filter_option or not search_input:
        return redirect(url_for('college.college'))

    try:
        colleges = CollegeModel.search_college(filter_option, search_input)
        if colleges:
            flash(f"Found {len(colleges)} result(s).", "success")
        else:
            flash("No results found.", "info")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")

    return render_template("college.html", add_form=add_form, colleges=colleges, page_name='colleges', filter_option=filter_option, search_input=search_input)