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
            try:
                result = CourseModel.add_course(collegeId, courseCode, courseName)
                if "successfully" in result:
                    flash(result, 'success')
                elif "duplicate" in result.lower():
                    flash("Course not created: Cannot have duplicate courses.", 'danger')
                else:
                    flash(result, 'danger')
            except Exception as e:
                if "Duplicate entry" in str(e):
                    flash("Course not created: Cannot have duplicate courses.", 'danger')
            return redirect(url_for('course.course'))
        else:
            for field_name, errors in add_form.errors.items():
                for error in errors:
                    field_label = getattr(add_form, field_name).label.text
                    flash(f"Course not created: {field_label} {error}", 'danger')

            # flash('Course not created!', 'danger')

    colleges = CollegeModel.get_college_codes()
    courses = CourseModel.get_courses()
    return render_template("course.html", add_form=add_form, colleges=colleges, courses=courses)

@course.route('/update_course', methods=['GET', 'POST'])
def update_course():
    if request.method == "POST":
        newCode = request.form.get('code')
        name = request.form.get('name')
        college = request.form.get('college')
        oldCode = request.form.get('hiddenCode')

        result = CourseModel.update_course(newCode, name, college, oldCode)

        if "successfully" in result:
            flash(result, 'success')
        else:
            flash(result, 'danger')
    return redirect(url_for('course.course'))
    # else:
    #     flash('Course information NOT updated!', 'danger')

@course.route('/delete_course', methods=['POST'])
def delete_course():
    if request.method == "POST":
        course_code = request.form['code']
        if course_code:
            result = CourseModel.delete_course(course_code)
            flash(result, 'success')
        return redirect(url_for("course.course"))
    else:
        flash('Course NOT deleted!', 'danger')
    
@course.route('/search_course', methods=['GET', 'POST'])
def search_course():
    add_form = AddCourseForm()

    filter_option = request.form.get('course_filter')
    course_search_input = request.form.get('course_search_input')

    if not filter_option or not course_search_input:
        return redirect(url_for('course.course'))

    try:
        courses = CourseModel.search_course(filter_option, course_search_input)
        if courses:
            flash(f"Found {len(courses)} result(s).", "success")
        else:
            flash("No results found.", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")

    return render_template("course.html", add_form=add_form, courses=courses, page_name='colleges', filter_option=filter_option, course_search_input=course_search_input)
