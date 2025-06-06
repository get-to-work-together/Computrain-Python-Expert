from python_expert.models.user import User, get_users

from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static')

@app.route("/")
def hello_world():
    return "<h1>Welcome to my users webpage</h1>"

@app.route("/hello")
def hello():
    name = request.args.get('name') or 'Stranger'
    return f"<h1>Hello {name}<h1>"

@app.route("/users")
def users():
    name = request.args.get('name') or None
    e_mail = request.args.get('e_mail') or None
    group = request.args.get('group') or None
    data = get_users(name=name, e_mail=e_mail, group=group)
    return render_template('users.html', title='Users', data=data)

@app.route("/api/v1/users")
def api_users():
    name = request.args.get('name') or None
    e_mail = request.args.get('e_mail') or None
    group = request.args.get('group') or None
    data = get_users(name=name, e_mail=e_mail, group=group)
    return [user.to_json() for user in data]


app.run(debug=True)