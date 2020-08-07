from flask import (
    Blueprint, Flask, flash, jsonify, redirect, render_template,session, request,
    session, url_for)

from helpers.auth import *
from Catalogger import app

mod = Blueprint('auth', __name__, url_prefix='')

@mod.route("/")
def register_page():
    return render_template('auth/register1.html')

# REGISTER USER ------------------------------------------------------------------------------ 
@mod.route("/register_user",methods=["POST"])
def register_user():
    user_id = createUserAccount(request.form['name'],request.form['email'],request.form['pass'])
    if(user_id):
        return render_template('home/index.html')
    else:
        return redirect("/")

# REGISTER BUSINESS USER ---------------------------------------------------------------------- 
@mod.route("/register_business_user",methods=["POST"])
def register_business_user():
    business_user_id = createBusinessUserAccount(request.form['name'],request.form['email'],request.form['pass'],request.form['bname'],request.form['category'])
    if(business_user_id):
        return render_template('home/index.html')
    else:
        return redirect("/")

@mod.route("/loginPage")
def login_page():
    return render_template('auth/login1.html')

@mod.route("/registerPage")
def registerPage():
    return render_template('auth/register1.html')

# USER LOGIN ---------------------------------------------------------------------------------- 
@mod.route("/login_user",methods=["POST"])
def login_user():
    login_id = loginUserAccount(request.form['email'],request.form['pass'])
    if(login_id):
        session[uid] = userId
        return render_template('home/index.html')
    else:
        flash('Invalid credentials', 'danger')
        return redirect("/loginPage")

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

@mod.route("/logout")
def logout_user():
    try:
        session.pop('uid',None)
        session.pop('category',None)
        session.pop('name',None)
        return redirect('/home')
    except:
        return redirect('/home')
