from flask import Flask, render_template, request, send_from_directory, redirect, flash
from tables import *
from checkpath import *
from jinja2 import Environment, FileSystemLoader

file_loader=FileSystemLoader('templates')
env = Environment(loader=file_loader)

ALLOWED_EXTENSIONS = {'ods', 'xml'}

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

@app.route('/upload', methods=['GET', 'POST'])
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
            #return '<!DOCTYPE html> <html lang="ru"><head><title>'+file.filename +'</title><meta charset="utf-8"> <style>table {border-collapse:collapse;}</style> </head><body>' + tableManipulations(file.filename, 'Имя', "Фамилия") + '</body></html>'
            tm = env.get_template('upload.html')
            table = tableManipulations(file.filename, 'Имя', "Фамилия")
            return tm.render(file = file, table= table)
        return render_template("index.html")