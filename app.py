from flask import Flask

app = Flask(__name__)


@app.route('/')
def base_page():  # put application's code here
    return 'Миссия Колонизация Марса'

@app.route("/index")
def index_page():
    return "И на Марсе будут яблони цвести!"

@app.route("/promotion")
def promotion_page():
    text = """Человечество вырастает из детства.</br>
    Человечеству мала одна планета.</br>
    Мы сделаем обитаемыми безжизненные пока планеты.</br>
    И начнем с Марса! Присоединяйся!"""
    return text


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
