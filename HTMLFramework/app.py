from flask import Flask, render_template, request
app = Flask(__name__)

#Main Screen
@app.route('/')
def home():
    return render_template('index.html')

#Student and Staff Registration
@app.route('/form_reg')
def regis():
    return render_template('SSReg.html') 

#Student and Staff Login
@app.route('/new')
def new_user():
    return render_template("SSLogin.html")
database={'22137553@dut4life.ac.za':'1234', '22113344': '12345'}

#Student and Staff Testing Login
@app.route('/form_login',methods=['POST','GET'])
def profile():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('SSLogin.html', info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('SSLogin.html', info='Invalid Password')
        else:
            return render_template('SSMenu.html')



#Maintenance Login
#@app.route('/new')
#def new_user():
#    return render_template("mainLogin.html")
#database={'bmw@bmw.com':'1234', 'audi@audi.com': 12345}


if __name__ == '__main__':
    app.run(debug=True)
