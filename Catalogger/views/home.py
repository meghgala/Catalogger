from flask import (
    Blueprint, Flask, flash, jsonify, redirect, render_template,session, request,
    session, url_for)

from helpers.auth import *
from Catalogger import app

mod = Blueprint('home', __name__, url_prefix='/home')

@mod.route("/")
def home_page():
    bname = session['business']['business_name']
    bdesc = session['business']['business_description']
    categories = getBusinessCategories(session['business']['business_id'])
    return render_template('category/category.html', categories = categories, bname = bname, bdesc = bdesc)

