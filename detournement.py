"""
Application Flask qui redirige sur differentes pages pour obtenir le flag

flag = RS{734M_JU1}
"""
### Import des modules
from flask import Flask, render_template, redirect, url_for, request, abort

### Parametrages de Flask
app = Flask(__name__, template_folder="templates")

### Code pour la redirection
@app.route('/')
def home():
    return redirect('/R')

@app.route('/R')
def R():
    return redirect('/S')

@app.route('/S')
def S():
    return redirect('/{')

@app.route('/{')
def open():
    return redirect('/7')

@app.route('/7')
def seven():
    return redirect('/3')

@app.route('/3')
def three():
    return redirect('/4')

@app.route('/4')
def four():
    return redirect('/M')

@app.route('/M')
def m():
    return redirect('/_')

@app.route('/_')
def bracket():
    return redirect('/J')

@app.route('/J')
def j():
    return redirect('/U')

@app.route('/U')
def u():
    return redirect('/1')

@app.route('/1')
def one():
    return redirect('/}')

@app.route('/}')
def close():
    return redirect('/R')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
