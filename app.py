from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    resultado = ''

    if request.method == 'POST':
        try: 
            n1 = float(request.form['num1'])
            n2 = float(request.form['num2'])
            operacion = request.form['operacion']

            if operacion == 'sumar':
                resultado = n1 + n2
            elif operacion == 'restar':
                resultado = n1 - n2
            elif operacion == 'multiplicar':
                resultado = n1 * n2
            elif operacion == 'dividir':
                resultado = n1 / n2 if n2 != 0 else 'Error: division por cero'
        except:
            resultado = 'Error en los datos'
    return render_template('index.html', resultado=resultado)
if __name__ == '__main__':
    app.run(debug=True)