from flask import Flask, render_template
from flask.templating import render_template 
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def hi(name):
    return "Hi " + str(name)

@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    
    return str(word) * int(num)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/noodles') 
def noodles():
    return render_template('noodles.html')

@app.route('/andco')
def andco():
    return render_template('andco.html')

if __name__=="__main__":  
    app.run(debug=True) 
    