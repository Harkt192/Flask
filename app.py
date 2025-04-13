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

@app.route("/image_mars")
def image_mars_page():
    return r"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/images/mars.png" />
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8000, host="127.0.0.1")
