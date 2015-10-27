from flask import Flask, render_template, json, request
from login import login
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
        valid = login.login(username, password)
        if valid:
            return redirect(url_for('main'))
        else:
            flash('Invalid login')
            return redirect(url_for('index'))
    else:
        return abort(405)

if __name__ == "__main__":
    app.run()

