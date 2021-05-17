import unittest, os
from app import app, db
from app.models import User, Score

class modelCase(unittest.TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config["SQLALCHEMY_DATABASE_URI"]=\
            'sqlite:///'+os.path.join(basedir, 'test.db')
        self.app = app.test_client() #create a virtual test environment
        db.create_all()
        u1 = User(id='1',username='user1',email='test1@gmail.com',password_hash='12345678')
        u2 = User(id='2',username='user2',email='test2@gmail.com',password_hash='12345678')
        s = Score(id='0',username='user1',score='100',accuracy='100.0',user_id='1')

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(s)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_password_hashing(self):
        u = User.query.get('12345678')
        u.set_password('test1234')
        self.assertFalse(u.check_password('case1234'))
        self.assertTrue(u.check_password('test1234'))

    def test_is_committed(self):
        u = User.query.get('1')
        self.assertFalse(u.is_committed())
        u2 = User.query.get('2')
        s = Score.query.first()
        db.session.add(s)
        db.session.flush()
        db.session.commit()
        self.assertTrue(s.is_committed())

