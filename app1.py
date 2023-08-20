from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index2.html",content=["virat","rohith","dhawan"])


if __name__ == "__main__":
    app.debug=True
    app.run()