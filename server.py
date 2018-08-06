from flask import Flask, redirect, render_template, session, request
import random
theNumber = random.randint(0,101)
app = Flask(__name__)
app.secret_key = 'ascnwoen?aijpnnwfwf3*^%$ac'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['guess'] = request.form['guess']
    guess = session['guess']
    print guess
    return redirect('/')

app.run(debug=True)