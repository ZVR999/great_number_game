from flask import Flask, redirect, render_template, session, request
import random
theNumber = random.randint(0,101)
app = Flask(__name__)
app.secret_key = 'asc14$@en?aijpnnwfwf3*^%$ac'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    session['res'] = ''
    theNumber = random.randint(0,101)
    return redirect('/')

@app.route('/process', methods=['POST'])
def process():
    session['res'] = ''
    session['response'] = ''
    session['guess'] = request.form['guess']
    session['num'] = str(theNumber)
    session['theNumber'] = int(theNumber)

    if session['guess'] == '':
        session['response'] = 'Please enter a number'
        print session['response']
        return redirect('/')
    session['guess'] = int(session['guess'])
    print theNumber
    
    if session['guess'] > theNumber:
        session['response'] = 'Too High!'
        print session['response']
        session['res'] = '<div class="response">Too High!</div>'
        return redirect('/')
    elif session['guess'] < theNumber:
        session['response'] = 'Too Low!'
        session['res'] = '<div class="response">Too Low!</div>'
        print session['response']
        return redirect('/')
    elif session['guess'] == theNumber:
        session['response'] = session['num']+' was the number!'
        session['res'] = '<div class="correct">'+session['response']+'</div>'
        session['res'] += '<form action="" method="POST"> <button type="submit">Play Again?</button></form>'  
        print session['response']
        return redirect('/')

app.run(debug=True)