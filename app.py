from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []


@app.route('/')
def homepage():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
