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

    if request.method == 'POST':
        if add_form.validate_on_submit():
            studentId = add_form.studentIdInput.data
            studentFirstname = add_form.studentFirstnameInput.data
            studentLastname = add_form.studentLastnameInput.data
            studentCourse = add_form.studentCourseInput.data
            studentYear = add_form.studentYearInput.data
            studentGender = add_form.studentGenderInput.data

            result = StudentModel.add_student(studentId, studentFirstname, studentLastname, studentCourse, studentYear, studentGender)
            flash(result, 'success')

            return redirect(url_for('student.students'))
        else:
            flash('Student NOT created!', 'danger')

    students = StudentModel.get_students()
    return render_template("student.html", add_form=add_form, students=students)

@student.route('/update_student', methods=['GET','POST'])
def update_student():
    if request.method == 'POST':
        id = request.form['code']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']
        
        result = StudentModel.update_student(id, firstname, lastname, course, year, gender)
        flash(result, 'success')

        return redirect(url_for('student.students'))
    else:
        flash('Student information NOT updated!', 'danger')

@student.route('/delete_student', methods=['POST'])
def delete_student():
    if request.method == "POST":
        student_id = request.form['code']
        if student_id:
            result = StudentModel.delete_student(student_id)
            flash(result, 'success')

        return redirect(url_for("student.students"))
    else:
        flash('Student NOT deleted!', 'danger')
    
@student.route('/search_student', methods=['GET', 'POST'])
def search_student():
    add_form = AddStudentForm()

    filter_option = request.form.get('student_filter')
    student_search_input = request.form.get('student_search_input')

    if not filter_option or not student_search_input:
        return redirect(url_for('student.students'))
    
    try:
        students = StudentModel.search_student(filter_option, student_search_input)
        if students:
            flash(f"Found {len(students)} result(s).", "success")
        else:
            flash("No results found.", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return render_template("student.html", add_form=add_form, students=students, filter_option=filter_option, student_search_input=student_search_input)