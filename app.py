from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá, Mundo!"

@app.route('/info')
def info():
    modulo = "Flask"
    aula = 1
    return f"<h1>Módulo: {modulo}, Aula: {int(aula)}</h1>"

@app.route('/bemvindo/<usuario>')
def bemvindo(usuario):
    return f"Bem Vindo(a) {usuario.captalize()}!"