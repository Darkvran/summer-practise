from flask import Flask, render_template, request, send_from_directory, redirect, flash
from tables import *


ALLOWED_EXTENSIONS = {'ods'}

app = Flask(__name__)

def tableManipulations(filename, colToReplace1, colToReplace2):
    table = readEx(filename)
    table = replaceCols(table, colToReplace1, colToReplace2)
    table = numerateRows(table)
    return genHtmlTable(table)
@app.route("/")
def indexhtml():
    return render_template("index.html")
@app.route('/static/&lt;path:path&gt;')
def send_static(path):
    return send_from_directory('static', path)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            return tableManipulations(file.filename, 'Имя', "Фамилия")
        return render_template("index.html")