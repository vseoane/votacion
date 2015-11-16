from flask import Flask, render_template, json, request, redirect, url_for, flash
from votacion.login import login as loginator
import os
from flask import Flask, render_template
import random
# imports for Bokeh plotting
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, components
# imports for matplotlib plotting
import tempfile
import matplotlib
matplotlib.use('Agg')  # this allows PNG plotting
import matplotlib.pyplot as plt

app = Flask(__name__)
user = None

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
            user = username
            return main_screen()
        else:
            #flash('Invalid login')
            return index_screen()

@app.route('/main', methods=['GET', 'POST'])
def main_screen():
    if user == None:
        return render_template('index.html')
    return render_template('main.html')

@app.route('/index', methods=['GET', 'POST'])
def index_screen():
    if user == None:
        return render_template('index.html')
    return render_template('index.html')

@app.route('/graficos')
def indexPage():
    if user == None:
        return render_template('index.html')
    # generate some random integers, sorted
    exponent = .7 + random.random() * .6
    dta = []
    for i in range(50):
        rnum = int((random.random() * 10) ** exponent)
        dta.append(rnum)
    y = sorted(dta)
    x = range(len(y))
    # generate Bokeh HTML elements
    # create a `figure` object
    p = figure(title='A Bokeh plot',
               plot_width=500, plot_height=400)  # add the line
    p.line(x, y)
    # add axis labels
    # p.xaxis.axis_label = "Candidatos"
    # p.yaxis.axis_label = "Votos"
    # create the HTML elements to pass to template
    figJS,figDiv = components(p,CDN)
    # generate matplotlib plot
    fig = plt.figure(figsize=(5, 4), dpi=100)
    axes = fig.add_subplot(1, 1, 1)
    # plot the data
    #axes.plot(x, y, '-')
    axes.bar(x, y)
    # labels
    axes.set_xlabel('Candidatos')
    axes.set_ylabel('Votos')
    axes.set_title("Votos por candidato")  # make the temporary file
    f = tempfile.NamedTemporaryFile(
        dir=os.path.dirname(__file__)+'/static/temp',
        suffix='.png', delete=False)
    # save the figure to the temporary file
    plt.savefig(f.name)
    f.close()  # close the file
    # get the file's name (rather than the whole path) # (the template will need that)
    plotPng = f.name.split('/')[-1]
    return (render_template(
        'graficos.html',
        y=y,
        figJS=figJS, figDiv=figDiv,
        plotPng=plotPng))

@app.route('/resultados')
def verResultados():
    if user == None:
        return render_template('index.html')
    # generate some random integers, sorted
    exponent = .7 + random.random() * .6
    dta = []
    for i in range(50):
        rnum = int((random.random() * 10) ** exponent)
        dta.append(rnum)
    y = sorted(dta)
    x = range(len(y))
    return (render_template(
        'resultados.html',
        y=y))

@app.route('/resultados_completos')
def verResultados_completos():
    if user == None:
        return render_template('index.html')
    # generate some random integers, sorted
    exponent = .7 + random.random() * .6
    dta = []
    for i in range(50):
        rnum = int((random.random() * 10) ** exponent)
        dta.append(rnum)
    y = sorted(dta)
    x = range(len(y))
    # generate Bokeh HTML elements
    # create a `figure` object
    p = figure(title='A Bokeh plot',
               plot_width=500, plot_height=400)  # add the line
    p.line(x, y)
    # add axis labels
    p.xaxis.axis_label = "Candidatos"
    p.yaxis.axis_label = "Votos"
    # create the HTML elements to pass to template
    figJS,figDiv = components(p,CDN)
    # generate matplotlib plot
    fig = plt.figure(figsize=(5, 4), dpi=100)
    axes = fig.add_subplot(1, 1, 1)
    # plot the data
    axes.plot(x, y, '-')
    # labels
    axes.set_xlabel('Candidatos')
    axes.set_ylabel('Votos')
    axes.set_title("Votos por candidato")  # make the temporary file
    f = tempfile.NamedTemporaryFile(
        dir=os.path.dirname(__file__)+'/static/temp',
        suffix='.png', delete=False)
    # save the figure to the temporary file
    plt.savefig(f.name)
    f.close()  # close the file
    # get the file's name (rather than the whole path) # (the template will need that)
    plotPng = f.name.split('/')[-1]
    return (render_template(
        'resultados_completos.html',
        y=y,
        figJS=figJS, figDiv=figDiv,
        plotPng=plotPng))


if __name__ == "__main__":
    app.run()

