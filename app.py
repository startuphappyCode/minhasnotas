# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # Nova rota
def main():
    resultado = None
    media = None

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')
    terceira = request.args.get('terceira')
    quarta = request.args.get('quarta')


    if primeira and segunda and terceira and quarta:
        primeira = float(primeira.replace(",","."))
        segunda = float(segunda.replace(",","."))
        terceira = float(terceira.replace(",","."))
        quarta = float(quarta.replace(",","."))

        media = (primeira + segunda + terceira + quarta) / 4
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media,
                           resultado=resultado)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
