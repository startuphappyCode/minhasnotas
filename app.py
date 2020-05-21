# -*- coding: utf-8 -*-
from flask import Flask, request, render_template # Importa a biblioteca


app = Flask(__name__) # Inicializa a aplicação

@app.route('/',  methods=['GET', 'POST']) # Nova rota
def main():
    resultado = None
    media = None

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')
    terceira = request.args.get('terceira')
    quarta = request.args.get('quarta')

    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)
        terceira = float(terceira)
        quarta = float(quarta)


        media = (primeira + segunda + terceira + quarta) / 2
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return render_template('index.html', media=media,
                                         resultado=resultado)

if __name__ == '__main__':
   app.run(debug=True)
