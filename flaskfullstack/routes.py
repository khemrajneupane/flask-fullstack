from flask import Flask, render_template, url_for, flash, redirect
from flaskfullstack import app, db,bcrypt
from flaskfullstack.forms import RegistrationForm, LoginForm
from flaskfullstack.models import User, Post
from flask_login import login_user,current_user, logout_user



posts = [
    {
        'author': 'Khemraj Neupane',
        'title': 'My title 1',
        'content': 'Welcome to my first post',
        'date_posted': '17 March, 2020'
    },
    {
        'author': 'Babita Gartaula',
        'title': 'Gartaula title 2',
        'content': 'Here is Babita post',
        'date_posted': '19 March, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_passord = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_passord)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:    
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))