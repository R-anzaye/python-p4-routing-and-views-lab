
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h1>{parameter}</h1>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ''.join(f'{i}<br>' for i in range(parameter))
    return f'<h1>{numbers}</h1>'


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h1>Invalid operation. Use +, -, *, div, or %.</h1>'
    
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
