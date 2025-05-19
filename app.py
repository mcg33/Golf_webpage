from flask import Flask, render_template, request
from load_db import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#Dynamic route to display a specific page
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f"Welcome, {username}!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not name or not email or not password:
            error_msg: str = "PLEASE FILL ALL FIELDS"
            return render_template('register.html', error=error_msg, name=name, email=email)

        #In absence of saving information to a database, we will just display success page
        return render_template('success.html', name=name)
    
    return render_template('register.html')

view_counter: int = 0

@app.route('/view_count')
def view_count():
    global view_counter
    view_counter += 1
    return f"Page total view count: {view_counter}"

@app.route('/welcome')
def welcome():
    return render_template(
        'welcome.html',
        message="Don't hit it into the water!"
        )

@app.route('/members')
def members_view():
    member = db[0]
    return render_template("members.html", members=member)

if __name__ == '__main__':
    app.run(debug=True)