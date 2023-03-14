from flask import Flask, render_template, request, redirect, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = "mysecretkey" #Choose Secret Key For Encryption

#MySQL Connection Settings
db = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)
cursor = db.cursor()

#Student & Staff Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash("Passwords do not match!", 'error')
            return redirect('/register')
        cursor.execute("INSERT INTO students (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        db.commit()
        flash("Registration successful!", 'success')
        return redirect('/login')
    return render_template('register.html')

#Student & Staff Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute("SELECT * FROM students WHERE email = %s AND password = %s", (email, password))
        student = cursor.fetchone()
        if student:
            session['student_id'] = student[0]
            session['student_name'] = student[1]
            flash("Login successful!", 'success')
            return redirect('/profile')
        else:
            flash("Invalid email or password!", 'error')
            return redirect('/login')
    return render_template('login.html')

# Logout a student or Staff
@app.route('/logout')
def logout():
    session.pop('student_id', None)
    session.pop('student_name', None)
    return redirect('/login')

# Edit profile of a student or Staff
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'student_id' in session:
        student_id = session['student_id']
        cursor.execute("SELECT * FROM students WHERE id = %s", student_id)
        student = cursor.fetchone()
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            if password != confirm_password:
                flash("Passwords do not match!", 'error')
                return redirect('/profile')
            cursor.execute("UPDATE students SET name = %s, email = %s, password = %s WHERE id = %s", (name, email, password, student_id))
            db.commit()
            flash("Profile updated successfully!", 'success')
            return redirect('/profile')
        return render_template('profile.html', student=student)
    else:
        flash("You need to login first!", 'error')
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
