from datetime import datetime
from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'


db = SQLAlchemy(app)

class tbl_todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    autohor=db.Column(db.String(200),nullable=False)
    content=db.Column(db.String(500),nullable=False)
    content_date=db.Column(db.DateTime,default=datetime.utcnow)

 

data=[
    {
        'author':'ajay Singh Bisht',
        'title':'My first python with flask webapp',
        'content':'this is the content of flask web app',
        'date':'May 15, 2021'
    
    },
     {
        'author':'Bhawana Mehra',
        'title':'My second python with flask webapp',
        'content':'this is the content of flask web app',
        'date':'May 19, 2021'
    
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html',posts=data)
    #return jsonify(data)

@app.route('/about')
def about():
    return render_template('About.html',title="About")

@app.route ('/welcome/<name>')
def welcome(name):
        return "welcome " + name

@app.route('/todo',methods=['POST','GET'])
def todo():
    if request.method=="POST":
        auth=request.form['txtautohor']
        cont=request.form['txtcontent']
        val=tbl_todo(autohor=auth,content=cont)
        db.session.add(val)
        db.session.commit()
        return render_template('Home.html',posts=data)
    else:

        return render_template('todo.html',title="Todo")
   
app.run(debug=True,port=2020)
db.create_all()