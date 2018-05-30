#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
    
@app.route('/')
def index():
    path = '/home/shiyanlou/files'
    file_titles_list = []
    for filename in os.listdir(path):
        with open(filename) as f:
            for k, y in json.loads(f.read()).items():
                if  k == 'title':
                    file_titles_list.append(y)
    titles = {'title_list': file_titles_list}
    return render_template('index.html', titles=titles)



@app.errorhandler(404)
def no_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
