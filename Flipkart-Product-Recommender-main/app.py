from flask import Flask,request,render_template,redirect,url_for,session
from flask_session import Session
import logins
import product

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def main():
    return redirect("/login")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        psw = request.form['password']
        session["uname"] = uname
        if logins.loginuser(uname, psw):
            return redirect(url_for('model'))
        
    return render_template("login.html")

@app.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        genre = request.form['Pname']
        rec = product.recommender(genre)
        return render_template('output.html', recommendations=rec)
    elif session.get("uname"):
        return render_template('intro.html')


if __name__=="__main__":
    app.run(host='localhost',port=5000,debug=True)