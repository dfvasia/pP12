from flask import Flask
app = Flask(__name__)


@app.route('/hello/')
def index():
    return 'Hello world!'

app.run()