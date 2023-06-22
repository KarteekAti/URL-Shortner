from secrets import choice
from flask import Flask, flash, redirect ,render_template, request, jsonify, url_for
from database import db,Links

import datetime
from validator_collection import checkers
import pyperclip


app = Flask(__name__,instance_relative_config = False)
app.config.from_object('config.Config')     
token_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"


def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()
init_db()


@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template("home.html")


@app.route('/long',methods=['GET','POST'])
def encode():
    if request.method == 'POST':
        longurl = request.form['long-url']
        if "http" not in longurl:
            longurl = "http://"+longurl
        print(longurl)
        if not checkers.is_url(longurl):
            flash("Enter a Valid URL for eg: www.google.com or google.com","warning")
            return render_template('home.html')
        
        if request.form['custom-url'] != "":
            token = request.form['custom-url']
        else:
            token = "".join(choice(token_characters) for i in range(7))
        try:
            info = Links(longURL = longurl, shortURL = token)
            db.session.add(info)
            db.session.commit()
            print("Links Recieved")
            flash("Copied to Clipboard","success")
            pyperclip.copy("127.0.0.1:5000/"+token)
        except Exception as e:
            flash("Custom URL already exists.","danger")
            print(e)
    
    return render_template('home.html',token = token)



@app.route('/<short>',methods = ['GET','POST'])
def toLong(short):
    if request.method == 'GET':
        long = Links.hasShortURL(short)
        print(long)
        if long != None:
            return redirect(long)
    return redirect('/')

if __name__ == '__main__':
    app.run()
