import os
import pathlib
import requests

from flask import request, render_template, redirect, url_for, flash

from cloudinary.uploader import upload, destroy

from config import CLOUD_NAME

from . import student
from app.models.studentModel import StudentModel
from app.models.collegeModel import CollegeModel
from app.models.courseModel import CourseModel
from app.controller.student.forms import AddStudentForm

@student.route('/students', methods=['GET', 'POST'], endpoint='students')
def students():
    add_form = AddStudentForm()
    add_form.studentCollegeInput.choices = CollegeModel.get_college_codes()

    courses = CourseModel.get_courses()
    print("Sample course: ", courses[1][1])
    add_form.studentCourseInput.choices = [(course[1], course[1]) for course in courses]

    if request.method == 'POST':
        if add_form.validate_on_submit():
            studentId = add_form.studentIdInput.data
            studentFirstname = add_form.studentFirstnameInput.data
            studentLastname = add_form.studentLastnameInput.data
            studentCourse = add_form.studentCourseInput.data
            studentYear = add_form.studentYearInput.data
            studentGender = add_form.studentGenderInput.data

            profile_picture = request.files['profile_picture']
            if profile_picture:
                photo_upload = upload(profile_picture
                                      , folder='ssisStudentPhotos',
                                      overwrite=True,
                                      resource_type="image")
                profile_pic_url = photo_upload.get('url')
            else:
                profile_pic_url = ''

            result = StudentModel.add_student(studentId, studentFirstname, studentLastname, studentCourse, studentYear, studentGender, profile_pic_url)
            flash(result, 'success')

            return redirect(url_for('student.students'))
        # if not add_form.validate_on_submit():
        #     print("Validation errors:", add_form.errors)
        else:
            flash('Student NOT created!', 'danger')
        
    students = StudentModel.get_students()
    studentsWithCollege = []
    for student in students:
        course = student[3]
        college = CollegeModel.get_college_by_course_name(course)
        studentsWithCollege.append(student + (college,))
    print(studentsWithCollege[0][7][0][0])

    colleges = CollegeModel.get_college_codes()
    return render_template("student.html", add_form=add_form, students=studentsWithCollege, colleges=colleges, courses=courses)

@student.route('/update_student', methods=['GET','POST'])
def update_student():
    if request.method == 'POST':
        id = request.form['code']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']

        profile_picture = request.files['photoInput']
        if profile_picture:
            # delete the current profile picture from cloudinary
            profile_pic_url = StudentModel.get_profile_url(id)
            profile_cloudId = profile_pic_url.split("/", 7)[-1].split(".")[0]

            destroy(profile_cloudId)

            # upload the new profile picture
            photo_upload = upload(profile_picture,
                                  folder='ssisStudentPhotos',
                                  overwrite=True,
                                  resource_type="image")
            profile_pic_url = photo_upload.get('url')
        else:
            profile_pic_url = request.form.get('hiddenPhoto')
        
        result = StudentModel.update_student(id, firstname, lastname, course, year, gender, profile_pic_url)
        flash(result, 'success')

        return redirect(url_for('student.students'))
    else:
        flash('Student information NOT updated!', 'danger')

@student.route('/delete_student', methods=['POST'])
def delete_student():
    if request.method == "POST":
        student_id = request.form['code']
        if student_id:
            profile_pic_url = StudentModel.get_profile_url(student_id)
            profile_cloudId = profile_pic_url.split("/", 7)[-1].split(".")[0]

            destroy(profile_cloudId)

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
        studentsWithCollege = []
        for student in students:
            course = student[3]
            college = CollegeModel.get_college_by_course_name(course)
            studentsWithCollege.append(student + (college,))
        if students:
            flash(f"Found {len(students)} result(s).", "success")
        else:
            flash("No results found.", "danger")
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    
    return render_template("student.html", add_form=add_form, students=studentsWithCollege, filter_option=filter_option, student_search_input=student_search_input)