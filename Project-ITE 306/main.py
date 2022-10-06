from flask import Flask,redirect,request,url_for,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("SignUp.html")
@app.route("/home/<username>")
def home(username):
    return render_template("HomePage.html", user=username)
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        return redirect(url_for('home',username=username))
    else:
        user=request.args.get('user')
        return redirect(url_for('home',username=username))


if __name__=="__main__":
    app.run()