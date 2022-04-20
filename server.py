from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

# index.html route
@app.route('/users')
def index():
    # call the get all method to get all useres
    users = User.get_all()
    # prints users to terminal
    print(users)
    return render_template('users.html', users = users)

# new user form
@app.route('/new', methods=["POST"])
def new():
    return render_template('new.html')

# create user
@app.route('/create_user', methods=["POST"])
def create_user():
    # create a dict to store requests from form
    # keys in dict need to line up with variable name from /new
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # pass dict to save_user method from User class
    User.save_user(data)
    # redirect to index
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)