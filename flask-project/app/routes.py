import requests
from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.forms import LoginForm, MessageForm
from app.models import User, Message
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user


@myapp_obj.route('/')
def hello():
    if current_user.is_authenticated:
        messages = Message.query.filter(User.username == current_user.username).all()
        return render_template('home.html', messages=messages)
    else:
        # user is not logged in, show default splash page instead
        unsplash_access_key = {'Authorization': 'Client-ID xZxl5W67jLnaze7X0zMCWJeT5scsiMuwqsvGDCwFoZU'}
        unsplash_parameters = {'collections': '11649432',
                               'orientation': 'landscape'}
        unsplash_url = f'https://api.unsplash.com/photos/random'
        # r = requests.get(unsplash_url, params=unsplash_parameters, headers=unsplash_access_key).json()
        r = {'urls': {
            'raw': 'https://images.unsplash.com/photo-1543337212-8c58be380d9d?ixid=MnwzODUwNDd8MHwxfHJhbmRvbXx8fHx8fHx8fDE2Njk5MjYxMzA&amp;ixlib=rb-4.0.3'
        }}
        # print(r)
        # print(r.json())
        return render_template('splash.html', image_url=r['urls']['raw'], hidelogout = True)

@myapp_obj.route('/favorites/')
def favorites():
    if current_user.is_authenticated:
        favorite_messages = User.favorite_messages
        return render_template('favorites.html', messages=favorite_messages)


@myapp_obj.route('/like-message/<int:id>/')
def like(id):
    # toggle messages[id][liked]
    return redirect('/')


@myapp_obj.route('/logout/')
@login_required
def logout():
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
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login/')

        # login user
        login_user(user, remember=current_form.remember_me.data)
        print(current_form.username.data, current_form.password.data)
        return redirect('/')
    parameters = {"form": current_form, "hidelogout": True}

    return render_template('login.html', **parameters)


@myapp_obj.route('/message', methods=['POST', 'GET'])
def message():
    if not current_user.is_authenticated:
        return redirect('/login')

    current_form = MessageForm()
    if current_form.validate_on_submit():
        m = Message(contents=current_form.message.data, like_count=0, user_id=current_user.id)
        db.session.add(m)
        db.session.commit()
        return redirect('/')

    return render_template('message.html', form=current_form)
