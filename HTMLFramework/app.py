from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new')
def new_user():
    return render_template("mainLogin.html")

@app.route('/profile')
def profile():
    return render_template('mainReg.html')

if __name__ == '__main__':
    app.run(debug=True)