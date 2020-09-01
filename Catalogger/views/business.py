from flask import (
    Blueprint, Flask, flash, jsonify, redirect, render_template,session, request,
    session, url_for)

from helpers.category import *
from Catalogger import app
from helpers.auth import *

mod = Blueprint('', __name__, url_prefix='/business')

@mod.route("/<business_id>",methods=["GET","POST"])
def business_user(business_id):
    categories = getBusinessCategories(business_id)
    return render_template('category/user_category.html', categories = categories)

