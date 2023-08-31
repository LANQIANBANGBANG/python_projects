from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# #cursor.execute("INSERT OR IGNORE INTO books VALUES(2, '1984', 'Bob', '9.1')")
# db.commit()


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy()
db.init_app(app)

# create a table called
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# with app.app_context():
#     db.create_all()

# create books
# with app.app_context():
#     new_book = Book(id=1, title="Hello Katty", author="Mary",rating=7.3)
#     db.session.add(new_book)
#     db.session.commit()
# read all books

@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html", books = all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"],
                        author=request.form["author"],
                        rating=request.form["rating"])
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
        # print(all_books)
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    # IF ACCESSED VIA POST THEN THE RATING HAS BEEN EDITED
    if request.method == 'POST':
        book_id = request.form["id"]
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar_one()
            book_to_update.rating = request.form["new_rating"]
            db.session.commit()
            return redirect(url_for('home'))
    # IF ACCESSED VIA GET THEN THE EDIT FORM NEEDS TO BE PRESENTED
    book_id = request.args.get('id')
    with app.app_context():
        book_to_edit = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar_one()
    return render_template('edit.html', book=book_to_edit)

if __name__ == "__main__":
    app.run(debug=False)

