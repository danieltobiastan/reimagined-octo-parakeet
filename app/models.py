from datetime import datetime 
from app import login, db # imports the database from init
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin 

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    scores = db.relationship('Score', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float, index=True, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Score {}>'.format(self.score)

# access the sqlite in the shell -- sqlite3 app.db
# see users: select*from user;
# see scores: select*from score;
# DO NOT EVER DROP TABLE

# manually adding scores to test 
#>>> u = User.query.get(4)
#>>> u
#<User user>
#>>> s = Score(score='44.56', author=u)
#>>> db.session.add(s)
#>>> db.session.commit()

#select user_id, username, score from User,Score where User.id  == Score.user_id; (see all records)