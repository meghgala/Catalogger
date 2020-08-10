from flask import (
    Blueprint, Flask, flash, jsonify, redirect, render_template,session, request,
    session, url_for)

from helpers.product import *
from Catalogger import app

mod = Blueprint('product', __name__, url_prefix='/product')

@mod.route("/")
def all_products():
    business_id = 'auR8fFiq74wverMNK0Ve'
    category_id = 'GVhP0FhnI294bicVmKdT'
    sub_category_id = 'TqPufEzH9f9yuXQCa36S'
    product_list = getProductsInfo(business_id,category_id,sub_category_id)
    print(product_list)
    return render_template('product/product.html',product_list=product_list)

