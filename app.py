from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        result = f'Корни уравнения: x1 = {x1}, x2 = {x2}'
    elif discriminant == 0:
        x = -b / (2*a)
        result = f'Уравнение имеет один корень: x = {x}'
    else:
        result = 'Уравнение не имеет действительных корней'

    return result

if __name__ == '__main__':
    app.run(debug=True)
