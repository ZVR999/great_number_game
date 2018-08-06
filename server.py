from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = 'ascnwoen?aijpnnwfwf3*^%$ac'

@app.route('/')
def index():
    return render_template('index.html')
app.run(debug=True)