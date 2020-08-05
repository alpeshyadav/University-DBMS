# from os import environ
import OpenSSL.crypto
import datetime
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

SECRET = os.getenv('SECRET')
print(SECRET)
app = Flask(__name__)

engine = create_engine(SECRET)
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("layout.html")


@app.route("/student", methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        return render_template('student.html')

    sid = request.form.get("sid")
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    dob = request.form.get('dob')
    age = request.form.get('age')
    gender = request.form.get('gender')
    phno = request.form.get('phno')
    house_no = request.form.get('house_no')
    building = request.form.get('building')
    city = request.form.get('city')
    course_id = request.form.get('course_id')
    dept_id = request.form.get('dept_id')

    db.execute('INSERT INTO student VALUES (:sid, :fname, :lname, :dob, :age, :gender, :phno, :house_no, :building, :city, :course_id, :dept_id)',
               {'sid': sid, 'fname': fname, 'lname': lname, 'dob': dob, 'age': age, 'gender': gender, 'phno': phno, 'house_no': house_no, 'building': building, 'city': city, 'course_id': course_id, 'dept_id': dept_id})
    db.commit()
    return render_template("success.html")


@app.route("/faculty", methods=['GET', 'POST'])
def faculty():
    if request.method == 'GET':
        return render_template("faculty.html")
    fid = request.form.get('fid')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    salary = request.form.get('salary')
    designation = request.form.get('designation')
    course_id = request.form.get('course_id')
    dept_id = request.form.get('dept_id')
    project_id = request.form.get('project_id')
    db.execute('INSERT INTO faculty  VALUES (:fid, :fname, :lname, :dob, :gender, :salary, :designation, :course_id, :dept_id, :project_id)',
               {'fid': fid, 'fname': fname, 'lname': lname, 'dob': dob, 'gender': gender, 'salary': salary, 'designation': designation, 'course_id': course_id, 'dept_id': dept_id, 'project_id': project_id
                })
    db.commit()
    return render_template('success.html')


@app.route('/department', methods=['GET', 'POST'])
def department():
    if request.method == 'GET':
        return render_template('department.html')
    dept_id = request.form.get('dept_id')
    dept_name = request.form.get('dept_name')
    db.execute('INSERT INTO dept VALUES (:dept_name, :dept_id)',
               {"dept_id": dept_id, 'dept_name': dept_name})
    db.commit()
    return render_template("success.html")


@app.route('/course', methods=['GET', 'POST'])
def course():
    if request.method == 'GET':
        return render_template('course.html')

    course_id = request.form.get("course_id")
    name = request.form.get("name")
    db.execute('INSERT INTO course VALUES (:course_id, :name)',
               {"course_id": course_id, "name": name})
    db.commit()
    return render_template('success.html')


@app.route('/project', methods=['GET', 'post'])
def project():
    if request.method == 'GET':
        return render_template('project.html')
    project_id = request.form.get('project_id')
    project_name = request.form.get('project_name')
    db.execute('INSERT INTO project VALUES (:project_id, :project_name)',
               {"project_id": project_id, "project_name": project_name})
    db.commit()
    return render_template("success.html")


@app.route('/per_project', methods=['GET', 'post'])
def per_project():
    if request.method == 'GET':
        return render_template('project.html')
    fid = request.form.get('fid')
    project_id = request.form.get('project_id')
    start_date = request.form.get('start_date')
    no_of_hours = request.form.get('no_of_hours')
    db.execute('INSERT INTO per_project VALUES (:fid, :project_id, :start_date, :no_of_hours)',
               {"fid": fid, "project_id": project_id, 'start_date': start_date, 'no_of_hours': no_of_hours})
    db.commit()
    return render_template("success.html")


@app.route('/student_data')
def student_data():
    student = db.execute('SELECT * from student').fetchall()
    return render_template("student_data.html", student=student)


@app.route('/faculty_data')
def faculty_data():
    faculty = db.execute('SELECT * from faculty').fetchall()
    return render_template("faculty_data.html", faculty=faculty)
