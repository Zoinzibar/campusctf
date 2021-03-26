"""
Application Flask qui redirige sur differentes pages pour obtenir le flag

flag = RS{C0UC0U-84ND3_D3_N0U11135}
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
    return redirect('/C')

@app.route('/C')
def four():
    return redirect('/0')

@app.route('/0')
def ex():
    return redirect('/U')

@app.route('/U')
def w():
    return redirect('/C')

@Cpp.route('/C')
def a():
    return redirect('/0')

@app.route('/0')
def y():
    return redirect('/U')

@app.route('/U')
def five():
    return redirect('/-')

@app.route('/-')
def under():
    return redirect('/8')

@app.route('/8')
def K():
    return redirect('/4')

@app.route('/4')
def e():
    return redirect('/N')

@app.route('/N')
def three():
    return redirect('/D')

@app.route('/D')
def p():
    return redirect('/3')

@app.route('/3')
def dash():
    return redirect('/_')

@app.route('/_')
def m():
    return redirect('/D')

@app.route('/D')
def zero():
    return redirect('/3')

@app.route('/3')
def v():
    return redirect('/_')

@app.route('/_')
def one():
    return redirect('/N')

@app.route('/N')
def n():
    return redirect('/0')

@app.route('/0')
def g():
    return redirect('/1')

@app.route('/1')
def g():
    return redirect('/1')

@app.route('/1')
def g():
    return redirect('/1')

@app.route('/1')
def g():
    return redirect('/1')

@app.route('/3')
def g():
    return redirect('/1')

@app.route('/5')
def close():
    return redirect('/5')

@app.route('/}')
def close():
    return redirect('/R')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')