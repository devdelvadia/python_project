from flask import request, render_template, redirect
from flask.helpers import url_for
from .utils import verified
from . import admin

@admin.route('/', methods=['GET', 'POST'])
def login() -> str:
    if request.method == 'POST':
        redirect(url_for('homepage'))
    return render_template('index.html')


@admin.route('/admin/signup')
def signup() -> str:
    return render_template('signup.html')


@admin.route('/admin/confirm_identity', methods=['GET', 'POST'])
def confirm_identity() -> str:
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('passwordConfirmation')

    if verified(username, password, password2):
        return redirect(url_for('homepage'))
    return render_template('signup.html')