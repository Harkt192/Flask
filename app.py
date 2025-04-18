import flask

app = flask.Flask(__name__)

@app.route('/')
def base_page():
    return flask.render_template("base.html")

@app.route("/index")
def index_page():
    return flask.render_template("index.html")

@app.route("/promotion")
def promotion_page():
    return flask.render_template("promotion.html")

@app.route("/image_mars")
def image_mars_page():
    return flask.render_template("image_mars.html")

@app.route('/bootstrap_sample')
def bootstrap():
    return flask.render_template("bootstrap_sample.html")

@app.route("/promotion_image")
def promotion_image_page():
    return


if __name__ == '__main__':
    app.run(port=8000, host="127.0.0.1")
