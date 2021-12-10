from flask import Flask, render_template
from funtions import open_file, person_data
from models import Person

settings_main = "settings.json"
people_list = "candidates.json"
read_method = ["r", "w", "a"]

settings_app = open_file(settings_main, read_method[0], "utf-8")
person_data_user = person_data(people_list, read_method[0], "utf-8")
print(person_data_user)

app = Flask(__name__)


@app.route('/')
def is_online():
    if settings_app["online"] is True:
        return render_template("s_main.html", s_status="Приложение работает")
    else:
        return render_template("s_main.html", s_status="Приложение не работает")


@app.route('/candidate/<int:id_x>')
def candidate(id_x):
    print(id_x)
    idx = id_x + 1
    person_data_user_name = person_data_user[idx]["name"]
    person_data_user_position = person_data_user[idx]["position"]
    person_data_user_picture = person_data_user[idx]["picture"]
    person_data_user_skills = person_data_user[idx]["skills"]
    return render_template("p_candidate.html", person_data_user_name=person_data_user_name,
                           person_data_user_position=person_data_user_position,
                           person_data_user_picture=person_data_user_picture,
                           person_data_user_skills=person_data_user_skills)


# @app.route('/list/')
# def list():
#     return "<h1>Имя кандидата</h1> <p>Позиция кандидата</p> <img src={{картинка}} width=200/> <p>Навыки кандидата</p>"

app.run(debug=True)
