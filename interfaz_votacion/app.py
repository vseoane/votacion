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
        print valid
        if valid:
            return redirect(url_for('main'))
        else:
            flash('Invalid login')
            return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()

