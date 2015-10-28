from flask import Flask, render_template, json, request, redirect, url_for, flash
from login import login as loginator
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html', next=request.args.get('next'))
    elif request.method == 'POST':
        username = request.form['inputName']
        password = request.form['inputPassword']
        valid = loginator.login(username, password)
        if valid:
            return main_screen()
        else:
            #flash('Invalid login')
            return index_screen()

@app.route('/main', methods=['GET', 'POST'])
def main_screen():
    return render_template('main.html')

@app.route('/index', methods=['GET', 'POST'])
def index_screen():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

