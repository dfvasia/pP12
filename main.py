from flask import Flask
from funtions import open_file

settings_main = "settings.json"
read_method = ["r", "w", "a"]
# settings_app ={}

# settings_app.update(open_file(settings_main, read_method[0], "utf-8"))
settings_app = open_file(settings_main, read_method[0], "utf-8")

app = Flask(__name__)


@app.route('/')
def is_online():
    if settings_app["online"] is True:
        return "Приложение работает"
    else:
        return "Приложение не работает"


@app.route('/candidate/')
def candidate():
    return "<h1>Имя кандидата</h1> <p>Позиция кандидата</p> <img src=https://picsum.photos/200 width=200/> <p>Навыки кандидата</p>"

@app.route('/list/')
def list():
    return "<h1>Имя кандидата</h1> <p>Позиция кандидата</p> <img src={{картинка}} width=200/> <p>Навыки кандидата</p>"

app.run()
