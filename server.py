from flask import Flask, redirect, render_template, session, request
import random
theNumber = random.randint(0,101)
app = Flask(__name__)
app.secret_key = 'asc14$@en?aijpnnwfwf3*^%$ac'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['guess'] = request.form['guess']
    guess = int(session['guess'])
    print guess
    print theNumber
    
    session['response'] = ''
    response = session['response']
    
    if guess > theNumber:
        response = 'Too High!'
        print response
        return redirect('/')
    elif guess < theNumber:
        response = 'Too Low!'
        print response
        return redirect('/')
    elif guess == theNumber:
        response = str(theNumber)+' was the number!'
        print response
        return redirect('/')

app.run(debug=True)