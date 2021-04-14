from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/bye/')
@app.route('/bye/<username>')
def bye_user(username="none"):
    if username != "none":
        return (f"Пока, {username}!", f"Хорошего вам дня {username}!")[' ' in username]
    else:
        return "Дружок-пирожок, тобой выбран неправильный URL"
