from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)

    def __init__(self, username, email,password,name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User',foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.id


class Follow(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    follow_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    user = db.relationship('User',foreign_keys=user_id)
    follow = db.relationship('User',foreign_keys=follow_id)

    def __init__(self, follow_id, user_id):
        self.follow_id = follow_id
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.id
