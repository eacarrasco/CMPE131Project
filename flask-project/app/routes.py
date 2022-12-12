from sqlalchemy.exc import IntegrityError
import requests
from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.forms import LoginForm, RegisterForm, MessageForm, DeleteAccountForm, SearchForm
from app.models import User, Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user


@myapp_obj.route('/')
def hello():
    if current_user.is_authenticated:
        # User is logged in, display all messages
        messages = Message.query.all()
        return render_template('home.html', messages=messages, username=current_user.username)
    else:
        # user is not logged in, show default splash page instead
        unsplash_access_key = {'Authorization': 'Client-ID xZxl5W67jLnaze7X0zMCWJeT5scsiMuwqsvGDCwFoZU'}
        unsplash_parameters = {'collections': '11649432',
                               'orientation': 'landscape'}
        unsplash_url = f'https://api.unsplash.com/photos/random'
        r = requests.get(unsplash_url, params=unsplash_parameters, headers=unsplash_access_key).json()
        # r = {'urls': {
        #     'raw': 'https://images.unsplash.com/photo-1543337212-8c58be380d9d?ixid=MnwzODUwNDd8MHwxfHJhbmRvbXx8fHx8fHx8fDE2Njk5MjYxMzA&amp;ixlib=rb-4.0.3'
        # }}
        return render_template('splash.html', image_url=r['urls']['raw'], hidelogout=True)


@myapp_obj.route('/logout/')
@login_required
def logout():
    # Logs user out and redirects to splash page
    logout_user()
    return redirect('/')


@myapp_obj.route('/login/', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            if user is None:
                flash('Invalid Username')
            else:
                flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login/')

        # login user
        login_user(user, remember=current_form.remember_me.data)
        return redirect('/')
    parameters = {"form": current_form, "hidelogout": True}

    return render_template('login.html', **parameters)


@myapp_obj.route('/register/', methods=['POST', 'GET'])
def register():
    current_form = RegisterForm()
    # User clicks register and enters information
    if current_form.validate_on_submit():
        try:
            if len(current_form.password.data) == 0:
                raise TypeError
            user = User(username=current_form.username.data,
                        password=generate_password_hash(current_form.password.data))

            db.session.add(user)

            db.session.commit()
            flash('Account created successfully! Please Login..')
            return redirect('/login')
        except IntegrityError:
            flash('Username already exists!')
        except TypeError:
            flash('Password cannot be empty!!')
        return redirect('/register')
    parameters = {"form": current_form, "hidelogout": True}

    return render_template('register.html', **parameters)


@myapp_obj.route('/deleteaccount/', methods=['POST', 'GET'])
def deleteaccount():
    # Deletes user's account and redirects to registration page
    if not current_user.is_authenticated:
        return redirect('/login')

    current_form = DeleteAccountForm()
    if current_form.validate_on_submit():
        if current_user.check_password(current_form.password.data):
            db.session.delete(current_user)
            db.session.commit()

            return redirect('/register/')
        flash('Incorrect Password!')
        return redirect('/deleteaccount/')

    return render_template('deleteaccount.html', username=current_user.username, form=current_form)


@myapp_obj.route('/message/', methods=['POST', 'GET'])
def message():
    # User is logged in and clicks to send message, the system prompts the user to send a message
    if not current_user.is_authenticated:
        return redirect('/login')

    current_form = MessageForm()
    if current_form.validate_on_submit():
        m = Message(contents=current_form.message.data, user=current_user)
        db.session.add(m)
        db.session.commit()
        return redirect('/')

    return render_template('message.html', form=current_form)


@myapp_obj.route('/search/', methods=['POST', 'GET'])
def search():
    # User is logged in and clicks search, the system prompts the user to enter a search query
    if not current_user.is_authenticated:
        return redirect('/login')

    current_form = SearchForm()
    if current_form.validate_on_submit():
        if current_form.mode.data == 'Users':
            results = User.query.filter(User.username.contains(current_form.query.data)).all()
        else:
            results = Message.query.filter(Message.contents.contains(current_form.query.data)).all()
        return render_template('search.html', form=current_form, results=results)

    return render_template('search.html', form=current_form)
