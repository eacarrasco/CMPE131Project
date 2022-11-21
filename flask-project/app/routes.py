from app import myapp_obj
from flask import render_template, redirect
from app.forms import LoginForm


@myapp_obj.route('/')
def hello():
    demo_messages = [{'user': 'Mario', 'contents': 'It\'s-a me, Mario!'},
                     {'user': 'Luigi', 'contents': 'Yahoo!'},
                     {'user': 'Goomba', 'contents': '...'}]
    return render_template('home.html', messages=demo_messages)


@myapp_obj.route('/login/', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()

    if current_form.validate_on_submit():
        print(f'{current_form.username.data=}, {current_form.password.data=}, {current_form.remember_me.data=}')
        return redirect('/')

    return render_template('login.html', form=current_form)


@myapp_obj.route('/user/<string:username>/')
def username(username):
    return render_template('username.html', username=username)
