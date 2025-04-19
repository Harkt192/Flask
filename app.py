import flask
from Scripts.bottle import request

app = flask.Flask(__name__)

@app.route('/')
def base_page():
    return flask.render_template("main.html")

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
    return flask.render_template("promotion_image.html")

@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if flask.request.method == 'GET':
        return flask.render_template("astronaut_selection.html")
    elif flask.request.method == 'POST':
        print(flask.request.form['surname'])
        print(flask.request.form['name'])
        print(flask.request.form['email'])
        print(flask.request.form['class'])

        jobs = []
        for job in [
            "Research_engineer",
            "Builder_engineer",
            "Pilot",
            "Meteorologist",
            "Life_support_engineer",
            "Radiation_protection_engineer",
            "Doctor",
            "Exobiologist"
        ]:
            try:
                if flask.request.form[job]:
                    jobs.append(job)
            except Exception:
                pass
        print(jobs)
        print(flask.request.form['sex'])
        print(flask.request.form['about'])

        if flask.request.form['file']:
            print(flask.request.form['file'])
        else:
            print("No file")
        try:
            print(flask.request.form['accept'])
        except Exception:
            print("No accept")
        return "<h1>Форма отправлена</h1>"


if __name__ == '__main__':
    app.run(port=8000, host="127.0.0.1")
