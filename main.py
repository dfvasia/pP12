from flask import Flask, render_template, redirect, request
from funtions import open_file, person_data
from models import Person

settings_main = "settings.json"
people_list = "candidates.json"
read_method = ["r", "w", "a"]

settings_app = open_file(settings_main, read_method[0], "utf-8")
person_data_user = person_data(people_list, read_method[0], "utf-8")
app = Flask(__name__)


@app.route('/')
def is_online():
    if settings_app["online"] is True:
        return render_template("s_main.html", s_status="Приложение работает")
    else:
        return render_template("s_main.html", s_status="Приложение не работает")


@app.route('/candidate/<int:id_x>')
def candidate(id_x):
    while True:
        if 0 < id_x <= 7:
            idx = id_x -1
            id_x_t = id_x + 1
            person_data_user_name = person_data_user[idx].name
            person_data_user_position = person_data_user[idx].position
            person_data_user_picture = person_data_user[idx].picture_url
            person_data_user_skills = person_data_user[idx].skills
            if id_x == 7:
                id_x_t = 1
                return render_template("p_candidate.html", person_data_user_name=person_data_user_name,
                                   person_data_user_position=person_data_user_position,
                                   person_data_user_picture=person_data_user_picture,
                                   person_data_user_skills=person_data_user_skills, id_x_t=id_x_t)
            else:
                return render_template("p_candidate.html", person_data_user_name=person_data_user_name,
                                   person_data_user_position=person_data_user_position,
                                   person_data_user_picture=person_data_user_picture,
                                   person_data_user_skills=person_data_user_skills, id_x_t=id_x_t)

        else:
            return redirect("http://127.0.0.1:5000/candidate/1", code=302)


@app.route('/list/')
def list():
    list_person = person_data_user
    return render_template("list.html", list_person=list_person)

@app.route('/search/')
def p_search():
    p_search = request.args.get("name")
    list_person = person_data_user
    temp_search = {}
    if p_search:
        if settings_app["case-sensitive"] is False:
            p_s = p_search.lower()
            for person in list_person:
                if p_s in person.name.lower():
                    temp_search[person.id_p] = person.name
        else:
            for person in list_person:
                if p_search in person.name:
                    temp_search[person.id_p] = person.name

    return render_template("search.html", p_search=temp_search, temp_search=temp_search)


@app.route('/skill/')
def skills():
    list_person = person_data_user
    temp_search = set ()
    for person in list_person:
        temp_search.add(person.skills)
    return render_template("skill.html", p_search=temp_search)




@app.route('/skill/<skill>')
def p_skill(skill):
    list_person = person_data_user
    cnt = 0
    temp_search = {}
    p_s = skill.lower()
    for person in list_person:
        if p_s in person.skills.lower():
            temp_search[person.id_p] = person.name
            cnt += 1
            if settings_app["limit"] == cnt:
                return render_template("skill.html", p_search=temp_search, temp_search=temp_search)
    return render_template("search.html", p_search=temp_search, temp_search=temp_search)



app.run(debug=True)
