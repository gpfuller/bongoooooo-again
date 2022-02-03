from flask import Flask, redirect, request, render_template
from user import User
app = Flask(__name__)

@app.route('/users')
def read_all():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users = users)

@app.route('/user/new')
def new():
    return render_template('create.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    data = {
        "fname": request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']

    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)