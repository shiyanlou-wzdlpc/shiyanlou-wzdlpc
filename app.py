#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
    
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
