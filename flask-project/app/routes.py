from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user


@myapp_obj.route('/')
def hello():
    demo_messages = [{'user': 'Mario', 'contents': 'It\'s-a me, Mario!', 'liked': False},
                     {'user': 'Luigi', 'contents': 'Yahoo!', 'liked': True},
                     {'user': 'Goomba', 'contents': '...', 'liked': False}]
    return render_template('home.html', messages=demo_messages)

@myapp_obj.route('/like-message/<int:id>/')
def like(id):
    # toggle messages[id][liked]
    return redirect('/')

@myapp_obj.route('/logout')
@login_required
def logout():
    load_user(current_user)
    return redirect('/')

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        print(f'{current_form.username.data=}, {current_form.password.data=}, {current_form.remember_me.data=}')

        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login')

        # login user
        login_user(user, remember=current_form.remember_me.data)
        flash('quick way to debug')
        flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/')
    a = 1
    name = 'Carlos'
    return render_template('login.html', name=name, a=a, form=current_form)


@myapp_obj.route('/user/<string:username>/')
def username(username):
    return render_template('username.html', username=username)
