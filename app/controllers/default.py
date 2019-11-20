from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm


@app.route('/index/<user>')
@app.route('/', defaults={'user':None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)

    return render_template('form.html', form=form)



@app.route('/teste/<info>')
@app.route('/teste', defaults={"info":None})
def teste(info):

    #userRead = User.query.filter_by(username="Cleiton").first()
    userRead = User.query.filter_by(username="Cleiton").first()

    print(userRead.username)


    #user = User("Cleiton1", "cleiton@cleiton1","123456", "Cleiton1")

    #db.session.add(user)
    #db.session.commit()

    return "ok"


