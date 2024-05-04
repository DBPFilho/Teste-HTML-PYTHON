from flask import Flask, render_template, request
import os

app = Flask(__name__)

def calcular(entrada1, entrada2, operacao):
    if operacao == 'soma':
        return entrada1 + entrada2
    elif operacao == 'subtracao':
        return entrada1 - entrada2
    elif operacao == 'multiplicacao':
        return entrada1 * entrada2
    elif operacao == 'divisao':
        if entrada2 != 0:
            return entrada1 / entrada2
        else:
            return 'Erro: divisão por zero'

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        entrada1 = int(request.form['entrada1'])
        entrada2 = int(request.form['entrada2'])
        operacao = request.form['operacao']
        resultado = calcular(entrada1, entrada2, operacao)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

