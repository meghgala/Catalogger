from flask import (
    Blueprint, Flask, flash, jsonify, redirect, render_template, request,
    session, url_for)

from helpers.auth import *
from Catalogger import app

mod = Blueprint('auth', __name__, url_prefix='')

@mod.route("/")
def login_page():
    return render_template('auth/basic_elements.html')

@mod.route("/register_user",methods=["POST"])
def reg_page():
    user_id = createStudentAccount(request.form['name'],request.form['email'],request.form['pass'])
    print(user_id)
    return "success"

@mod.route("/changePassword")
def change_password():
    if 'uid' in session:
        return render_template('auth/changepassword.html',name=session['name'])
    return render_template('auth/login.html')

@mod.route("/changePass",methods=["POST"])
def change_pass():
    if 'uid' in session:
        if changePassword(request.form['curpass'],request.form['newpass'],session['uid']):
            flash('Password Changed','success')
            return render_template('auth/changepassword.html',name=session['name'])
        else:
            flash('Password Not Changed','danger')
            return render_template('auth/changepassword.html',name=session['name'])
    flash('Please Login','danger')
    return render_template('auth/login.html')

@mod.route("/loginUser",methods=["POST"])
def login_user():
    session.pop('uid',None)
    userData = loginUser(request.form['email'],request.form['password'])
    if userData:
        session['category'],session['uid'],session['name'] = userData['category'],userData['uid'],userData['name']
        try:
            _ = request.form['rememberMe']
            session.permanent = True
        except:
            session.permanent = False
        return redirect('/home')
    flash('Incorrect Credentials','danger')
    print("hello")
    return redirect('/')

@mod.route("/logout")
def logout_user():
    try:
        session.pop('uid',None)
        session.pop('category',None)
        session.pop('name',None)
        return redirect('/home')
    except:
        return redirect('/home')
