#!usr/bin/env python3
from flask import Flask, render_template, url_for
from datetime import datetime
from flask_slqalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update['TEMPLATES_AUTO_RELOAD'] = True
app.config.update['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/wzdlpc'
db = SQLAlchemy(app)

class File(db.model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey(category.id))
    category = db.relationship('Category')
    content = db.Column(db.Text)

    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File(name=%s)>' % self.title

class Category(db.model):
    __tablename__ = 'categiries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category(name=%s)>' % self.name

@app.route('/')
def index():
    pass

@app.route('/files/<int:file_id>')
def file(file_id):
    pass

@app.errorhandler(404)
def not_found(error):
    return render_tamplate('404.html', 404)

if __name__ == '__main__':
    app.run()
