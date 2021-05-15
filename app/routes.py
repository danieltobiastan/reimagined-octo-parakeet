from flask import render_template, flash, redirect, url_for, request, make_response, jsonify, g, session
from app import app, db # imports the app and db from init
from app.forms import LoginForm, RegisterForm # import form classes to be used here
from flask_login import current_user, login_user, logout_user, login_required 
from werkzeug.urls import url_parse
from app.models import User, Score # imports the user class 
import json 
# will need to import the scores class to commit the data here also

# home page, where game resides (undone - waiting to commit with actual app)
# then log the scores into the scores database

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# score page, users can see scores (undone)
@app.route('/scores', methods=['GET','POST'])
@login_required
def scores():
    if current_user.is_authenticated: 
        user_username = current_user.username
        user_iden = current_user.id
        myScore = Score.query.filter_by(user_id=user_iden).all()
        wpm, accuracy, count, high_score= 0,0,0,0
        for score in myScore:
            if (score.score > high_score):
                high_score = score.score
            count += 1
            accuracy += score.accuracy
            wpm += score.score
        avg_wpm, avg_accuracy = (format((wpm/count), '.2f')), (format((accuracy/count), '.2f'))

        #top10Score = Score.query.filter_by(user_id=user_iden).order_by(Score.score.desc()).limit(10).all()
        #print(top10Score)
    return render_template('scores.html', username = user_username, user_id=user_iden, myScore=myScore, count=count, avg_wpm=avg_wpm, avg_accuracy=avg_accuracy, high_score=high_score)

# registration page - linked with database, left with design
@app.route('/register', methods=['GET','POST']) 
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('New User ' + form.username.data + ' has been created')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
 
# login page - linked with database, left with design
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated: # if the user is already logged in
        return redirect(url_for('home')) # returns the user to the homepage
    form = LoginForm() # display the form 
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # querying the database and matching, completes the query by calling the first result
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login')) # resets the form
        login_user(user, remember=form.remember_me.data) # if correct, log in
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page) # send user back home
    return render_template('login.html', title='Sign In', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    scores = [
        {'author': user, 'score': '55.55 {0}'.format('WPM')},
        {'author': user, 'score': '77.77 {0}'.format('WPM')}
    ]
    return render_template('user.html', user=user, scores=scores)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/scoreupload', methods=['POST'])
def create_score():
    score_item = request.get_json()
    username = json.dumps(score_item[0].get("username")).strip('"')
    score = json.dumps(score_item[0].get("score")).strip('"')
    accuracy = json.dumps(score_item[0].get("accuracy")).strip('"')
    user_id = json.dumps(score_item[0].get("user_id")).strip('"')
    new_score = Score(username=username, score=float(score), accuracy=float(accuracy), user_id=int(user_id))
    db.session.add(new_score)
    db.session.commit()
    resp = make_response(jsonify({"message":"JSON Received"}), 200) # not neccesary code 
    return (resp) # not neccesary 

