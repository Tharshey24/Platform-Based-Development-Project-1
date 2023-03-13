from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Maintenance details of workers
workers = [
    {
        'username': 'Tharshey24',
        'password': '12345',
        'name': 'Tharshey Naidoo',
        'email': 'TharsheyN@Gmail.com'
    },
    {
        'username': 'Eshkar69',
        'password': '54321',
        'name': 'Eshkar Raj',
        'email': 'ER@gmail.com'
    }
]

# Login page
@app.route('/')
def login():
    return render_template('login.html')

# login submission
@app.route('/', methods=['POST'])
def login_submit():
    # Get logins
    username = request.form['username']
    password = request.form['password']

    # Check if valid
    for worker in workers:
        if worker['username'] == username and worker['password'] == password:
            # Store data
            session['worker'] = worker
            return redirect(url_for('profile'))
    
    # Invalid details
    error_message = "Invalid username or password."
    return render_template('login.html', error_message=error_message)

# Profile page
@app.route('/profile')
def profile():
    # Check if logged in
    if 'worker' not in session:
        return redirect(url_for('login'))

    # Get data
    worker = session['worker']
    return render_template('profile.html', worker=worker)

# Profile form submission
@app.route('/profile', methods=['POST'])
def profile_submit():
    # Check if logged in
    if 'worker' not in session:
        return redirect(url_for('login'))

    # Get data
    worker = session['worker']

    # Update data
    worker['name'] = request.form['name']
    worker['email'] = request.form['email']

    # Store updated data
    session['worker'] = worker

    # Display Success
    success_message = "Profile updated successfully."
    return render_template('profile.html', worker=worker, success_message=success_message)

# Logout
@app.route('/logout')
def logout():
    # Check if logged in
    if 'worker' not in session:
        return redirect(url_for('login'))

    # Clears the worker data
    session.pop('worker', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key = 'TestingKey' # Replace with secret key
    app.run(debug=True)
