from flask import Flask
import operator

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    return 'Привет жестокий мир'


@app.route('/bye/')
@app.route('/bye/<username>')
def bye_user(username="undefined"):
    if username != "undefined":
        return (f"Пока, {username}!", f"Хорошего вам дня {username}!")[' ' in username]
    else:
        return "Дружок-пирожок, тобой выбран неправильный URL"


@app.route('/<int:x>/<name_operation>/<int:y>')
def calculate(name_operation='undefined', x=0, y=0):
    operation_value = {
        'сумма': lambda x, y: x + y,
        'разность': lambda x, y: x - y,
        'умножение': lambda x, y: x * y,
        'деление': lambda x, y: x / y
    }[name_operation](x, y)
    return f"Результат {name_operation} равен {operation_value}"
