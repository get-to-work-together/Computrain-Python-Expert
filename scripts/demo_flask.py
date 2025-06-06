from python_expert.models.user import User, get_users

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!!!!!</h1>"

@app.route("/hello")
def hello():
    name = request.args.get('name') or 'Stranger'
    return f"<h1>Hello {name}<h1>"

@app.route("/webpage")
def webpage():
    name = request.args.get('name') or 'Stranger'
    return render_template('hello.html', name=name)

@app.route("/users")
def users():
    group = request.args.get('group') or None
    data = get_users(group=group)
    return render_template('list.html', title='Users', data=data)

app.run(debug=True)
