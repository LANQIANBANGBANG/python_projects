from flask import Flask, render_template, request,url_for,redirect
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/e75e0e49fccb076f6e84").json()

@app.route('/')
def index():
    #print(posts['title'])
    return render_template("index.html", all_posts=posts)

@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/receive_data", methods=['POST'])
# def submit_form():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#
#     return render_template("form_entry.html", submission_successful=True)


if __name__ == "__main__":
    app.run(debug=True)