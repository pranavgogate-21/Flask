from flask import Flask,render_template,redirect,url_for,request
from  flask import session
app=Flask(__name__)
app.secret_key="hello"
@app.route('/')
def home():
    return render_template("index1.html")

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        user=request.form["nm"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")
@app.route("/user")
def user():
    if "user" in session:
        user=session["user"]
        return f"<h1>HI, {user}<h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
if __name__=="__main__":
    app.debug=True
    app.run()
