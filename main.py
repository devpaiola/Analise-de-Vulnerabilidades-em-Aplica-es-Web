from flask import Flask, render_template, request, flash, redirect
import json



app = Flask(__name__)
app.config['SECRET_KEY'] = "palavra-secreta123"

@app.route('/') 
def home():
    return render_template('html/login.html')

if __name__ == "__main__":
    app.run(debug=True)