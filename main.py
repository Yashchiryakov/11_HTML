from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def page_index():
    return render_template("something.html")

app.run()