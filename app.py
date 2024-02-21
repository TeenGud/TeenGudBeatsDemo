from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///newflask.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    #picture = db.Column(db.LargeBinary, nullable=False)
    #music = db.Column(db.LargeBinary, nullable=True)


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        #picture = request.form['picture']
        #music = request.form['music']
        post = Post(title=title, text=text)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')

        except Exception as ex:
            print(ex)
            return "While creating the post some error has occurred"
    else:
        return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)