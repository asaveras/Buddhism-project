from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def page():
    with open('page.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def page2():
    with open('page2.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def page3():
    with open('page3.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return content
