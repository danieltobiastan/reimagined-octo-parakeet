from flask import render_template, flash, redirect, url_for, request
from app import app, db # imports the app and db from init
from app.forms import LoginForm, RegisterForm # import form classes to be used here
from flask_login import current_user, login_user, logout_user, login_required 
from werkzeug.urls import url_parse
from app.models import User # imports the user class 
# will need to import the scores class to commit the data here also

# home page, where game resides (undone - waiting to commit with actual app)
# then log the scores into the scores database
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# score page, users can see scores (undone)
@app.route('/scores')
@login_required
def scores():
    return render_template('scores.html')

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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
