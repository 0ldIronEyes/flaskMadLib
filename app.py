from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "SUPERSECRETKEY"

@app.route("/")
def fill_form():
    return render_template("",prompts=story.prompts)

@app.route("/story")
def showAdLib():
    story = story.generate(request.args)
    return render_template("story.html",storycontent=story)