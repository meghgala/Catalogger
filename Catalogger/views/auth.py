
from flask import (
    Blueprint, Flask, flash, jsonify, redirect, render_template,session, request,
    session, url_for)

from helpers.auth import *
from Catalogger import app

mod = Blueprint('auth', __name__, url_prefix='')

@mod.route("/")
def loginPage():
    return render_template('auth/login.html')

# REGISTER USER ------------------------------------------------------------------------------
@mod.route("/register_user",methods=["POST"])
def register_user():
    user_id = createUserAccount(request.form['name'],request.form['email'],request.form['pass'])
    if(user_id):
        return redirect('/home')
    else:
        return redirect("/")

# REGISTER BUSINESS USER ---------------------------------------------------------------------- 
@mod.route("/register_business_user",methods=["POST"])
def register_business_user():
    img = request.files.getlist("images")
    business_user_id = createBusinessUserAccount(request.form['name'],request.form['email'],request.form['pass'],request.form['bname'],request.form['bdesc'],request.form['getcategory'],img)
    if(business_user_id):
        return redirect('/home')
    else:
        return redirect("/")

@mod.route("/loginPage")
def login_page():
    return render_template('auth/login.html')

@mod.route("/userIndex")
def user_Index():
    return render_template('userIndex/userIndex.html')

@mod.route("/registerPage")
def registerPage():
    return render_template('auth/register.html')

# USER LOGIN ---------------------------------------------------------------------------------- 
@mod.route("/login_user",methods=["POST"])
def login_user():
    login_id = loginUserAccount(request.form['email'],request.form['pass'])
    if(login_id):
        session['uid'] = login_id
        session['business'] = getBusinessInfo(login_id)
        return redirect('/home')
    else:
        flash('Invalid credentials', 'danger')
        return redirect("/loginPage")

@mod.route("/search",methods=["POST"])
def search():
    search_result = searchProduct(request.form['search'])
    return render_template('userIndex/userIndex.html',search_result = search_result)

@mod.route("/logout")
def logout_user():
    try:
        session.pop('uid',None)
        session.pop('category',None)
        session.pop('name',None)
        return redirect('/home')
    except:
        return redirect('/home')
