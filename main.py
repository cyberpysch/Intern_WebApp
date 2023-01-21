from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///comment.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)


class Comment(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=='POST':
    
        title = request.form['title']
        comment = Comment(title=title)
        db.session.add(comment)
        db.session.commit()

    allComment = Comment.query.all()
    return render_template("index.html", allComment=allComment)

@app.route("/templates/ipl.html")
def ipl():
    allComment = Comment.query.all()
    return render_template("ipl.html",allComment=allComment)

@app.route("/templates/bpl.html")
def bpl():
    allComment = Comment.query.all()
    return render_template("bpl.html",allComment=allComment)


@app.route("/templates/test.html")
def test():
    allComment = Comment.query.all()
    return render_template("test.html",allComment=allComment)

@app.route("/templates/odi.html")
def odi():
    allComment = Comment.query.all()
    return render_template("odi.html",allComment=allComment)

@app.route("/templates/worldcup.html")
def worldcup():
    allComment = Comment.query.all()
    return render_template("worldcup.html",allComment=allComment)

@app.route("/templates/about.html")
def about():
    allComment = Comment.query.all()
    return render_template("about.html",allComment=allComment)

if __name__=="__main__":
    app.run(debug=False ,use_reloader=False)