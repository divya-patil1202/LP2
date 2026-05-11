

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def calculator():
    num1 = request.args.get('num1', default=0, type=float)
    num2 = request.args.get('num2', default=0, type=float)
    op = request.args.get('op', default='+')

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = "Cannot divide by zero" if num2 == 0 else num1 / num2
    else:
        result = "Invalid Operator"

    return f"Result = {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)