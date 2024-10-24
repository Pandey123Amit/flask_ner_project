import api
from db import database
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)
db = database()


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login' ,methods=['POST'])
def login():
    # Get form data
    email = request.form.get('email')
    password = request.form.get('password')
    respos = db.get_password(email)
    if password==respos:
        return render_template('main.html')
    else:
        return respos
@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/info', methods=['POST'])
def info():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    ids = request.form.get('id')

    # Insert data into the database
    response = db.insert(name, email, ids, password)

    # Check response and show messages accordingly
    if response:
        message = "Sign up successful! Please log in."
    else:
        message = "Email already exists. Please try another."

    return render_template('login.html', messages=[message])


@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['POST'])
def perform_ner():
    text = request.form.get('inputText')
    w=api.ner(text)
    print(w)
    return text



if __name__ == '__main__':
    app.run(debug=True)
