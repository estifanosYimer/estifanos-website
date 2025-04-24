# app.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you would handle form data or forward to Formspree/Netlify
        return redirect('/contact')
    return render_template('contact.html')

if __name__ == '__main__':
    import os
    app.run(debug=True, use_reloader=False)
