#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/wzdlpc'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    create_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)

    def __init__(self, title, created_time, category_id, content ):
        self.title = title
        self.created_time = created_time
        self.category_id = category_id
        self.content = content

    def __repr__(self):
        return '<File(title=%s)>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category(name=%s)>' % self.name



    
@app.route('/')
def index():
    path = '/home/shiyanlou/files'
    file_titles_list = []
    for jsonfile in os.listdir(path):
        with open(jsonfile) as f:
            for k, y in json.loads(f.read()).items():
                if  k == 'title':
                    file_titles_list.append(y)
    titles = {'title_list': file_titles_list}
    return render_template('index.html', titles=titles)

@app.route('/files/<filename>')
def file(filename):
    path = '/home/shiyanlou/files/' + filename
    if filename in os.listdir(path):
        return redirect(url_for('404.html'))
    else:
        with open(path) as f:
            readfile = json.loads(f.read())
        return render_template('file.html',readfile=readfile)



@app.errorhandler(404)
def no_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
