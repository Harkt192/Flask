import os
from os.path import exists

from flask import Flask, request, render_template, redirect
from forms.user import AstronautLoginForm
import random
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


PROFESSIONS = [
    "инженер-исследователь",
    "пилот",
    "строитель",
    "экзобиолог",
    "врач",
    "инженер по терраформированию",
    "климатолог",
    "специалист по радиальной защите",
    "астрогеолог",
    "гляциолог",
    "инженер жизнеобеспеченья",
    "метеоролог",
    "оператор марсохода",
    "киберинженер",
    "штурман",
    "пилот дронов"
]


@app.route('/')
def base_page():
    return render_template("main.html", title="Сайт")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AstronautLoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route("/distribution")
def distribution():
    people = [
        {"name": "Ридли Скотт", "status": "Капитан корабля"},
        {"name": "Энди Уир", "status": None},
        {"name": "Марк Уотни", "status": None},
        {"name": "Венката Капур", "status": None},
        {"name": "Тедди Сандерс", "status": None},
        {"name": "Шон Бир", "status": None}
    ]
    return render_template("distribution.html",
                           title="Distribution",
                           people=people)


# Почему-то, если добавить параметры через слеш ("/table/<string:sex>/<int:year>")
# то перестает работать загрузка изображений как и через html, так и через css
# поэтому приходиться так реализовывать, для ввода несольких параметров, нужно перейти на страницу типа:
# http://127.0.0.1:5000/table/male&16
@app.route("/table/<string:sex>&<int:year>")
def table(sex, year):
    g = hex(random.randint(0, 254))[2:].rjust(2, "0")
    if sex == "male":
        b = "FF"
        r = "00"
    else:
        b = "FF"
        r = "FF"
    color = r + g + b
    return render_template("table.html",
                           title="Оформление каюты",
                           color=color,
                           year=year
                           )


@app.route("/member")
def member():
    with open("templates/astronauts.json", "r", encoding="utf-8") as file:
        people = json.load(file)
    return render_template("member.html", title="Member", people=people)


@app.route("/index")
def index_page():
    return render_template("index.html")


@app.route("/promotion")
def promotion_page():
    return render_template("promotion.html")


@app.route("/image_mars")
def image_mars_page():
    return render_template("image_mars.html")


@app.route('/bootstrap_sample')
def bootstrap():
    return render_template("bootstrap_sample.html")


@app.route("/promotion_image")
def promotion_image_page():
    return render_template("promotion_image.html")


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template("astronaut_selection.html")
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])

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
                if request.form[job]:
                    jobs.append(job)
            except Exception:
                pass
        print(jobs)
        print(request.form['sex'])
        print(request.form['about'])

        if request.form['file']:
            print(request.form['file'])
        else:
            print("No file")
        try:
            print(request.form['accept'])
        except Exception:
            print("No accept")
        return "<h1>Форма отправлена</h1>"


@app.route("/choice/<string:planet_name>")
def choose_planet(planet_name):
    if planet_name == "Марс":
        return render_template("mars.html")
    elif planet_name == "Юпитер":
        return render_template("jupiter.html")


@app.route("/results/<string:nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return render_template(
        "results.html",
        nickname=nickname,
        level=level,
        rating=rating
    )


LAST_FILENAME = ""


@app.route('/load_photo', methods=["GET", "POST"])
def upload_file():
    global LAST_FILENAME
    filename = ""
    if request.method == "POST":
        if "file" not in request.files:
            if "send_file" in request.form:
                if not request.form["send_file"]:
                    return render_template('upload.html', message="Выберите файл", filename=filename)

        if "send_file" in request.form:
            temp_filename = request.form["send_file"]
            filename = temp_filename.replace("temp_", "")
            if not os.path.exists(
                    os.path.join("static/uploads", filename)
            ):
                os.rename(
                    os.path.join("static/uploads", temp_filename),
                    os.path.join("static/uploads", filename)
                )
            else:
                os.remove(
                    os.path.join("static/uploads", temp_filename)
                )
            LAST_FILENAME = ""
            return f"<h1>Файл {filename} успешно загружен.</h1><br><a href='/load_photo'>Загрузить ещё</a>"

        file = request.files["file"]
        filename = file.filename

        if file:
            if "file" in request.files:
                if LAST_FILENAME != "":
                    os.remove(
                        os.path.join("static/uploads", LAST_FILENAME)
                    )
                filename = "temp_" + filename
                temp_path = os.path.join("static/uploads", filename)
                file.save(temp_path)
                LAST_FILENAME = filename

    return render_template("upload.html", message="", filename=filename)


@app.route("/")
def carousel_page():
    carousel_images = [
        {"src": "images/mars_image_1.jpg",
         "alt": "Марс 1",
         "caption": "Первый слайд",
         "description": "Это очень красивый Марс"},
        {"src": "images/mars_image_2.png",
         "alt": "Марс 2",
         "caption": "Второй слайд",
         "description": "А этот ещё красивее"},
        {"src": "images/mars_image_3.jpg",
         "alt": "Марс 3",
        "caption": "Третий слайд",
         "description": "Этот неимоверно красивый"}
    ]
    return render_template("mars_carousel.html", carousel_images=carousel_images)

@app.route("/carousel")
def carousedasl_page():
    carousel_images = [
        {"src": "images/mars_image_1.jpg",
         "alt": "Марс 1",
         "caption": "Первый слайд",
         "description": "Это очень красивый Марс"},
        {"src": "images/mars_image_2.png",
         "alt": "Марс 2",
         "caption": "Второй слайд",
         "description": "А этот ещё красивее"},
        {"src": "images/mars_image_3.jpg",
         "alt": "Марс 3",
        "caption": "Третий слайд",
         "description": "Этот неимоверно красивый"}
    ]
    return render_template("carousel.html", carousel_images=carousel_images)


@app.route("/training/<string:speciality>")
def trainig_page(speciality):
    h2 = ""
    src = ""
    speciality = speciality.lower()
    if "инженер" in speciality:
        h2 = "Инжернерные тренажеры"
        src = "../static/images/house.jpg"
    elif "врач" in speciality:
        h2 = "Врачебные тренажеры"
        src = "../static/images/anatomy.jpg"
    else:
        h2 = "Научные симуляторы"
        src = "../static/images/spaceship.jpg"

    return render_template("training.html", h2=h2, src=src)


@app.route("/list_prof/<string:list_>")
def list_prof(list_):
    global PROFESSIONS
    return render_template("list_prof.html",
                           profs=PROFESSIONS,
                           par=list_)


app.run(port=8888, host="127.0.0.1")
