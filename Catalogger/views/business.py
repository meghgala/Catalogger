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
    return render_template('category/user_category.html',business_id = business_id, categories = categories)

@mod.route("/<business_id>/<categoryId>/<subcategoryId>",methods=["GET","POST"])
def business_user_product(business_id,categoryId,subcategoryId):
    categories = getBusinessCategories(business_id)
    product_list = getProductsInfo(business_id,categoryId,subcategoryId)
    return render_template('category/user_category.html',business_id = business_id, categories = categories, product_list = product_list)