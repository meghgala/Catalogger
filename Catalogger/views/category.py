from flask import (
    Blueprint, Flask, flash, jsonify, redirect, render_template,session, request,
    session, url_for)

from helpers.category import *
from Catalogger import app

mod = Blueprint('category', __name__, url_prefix='/category')

# @mod.route("/")
# def all_products():
#     business_id = 'auR8fFiq74wverMNK0Ve'
#     category_id = 'GVhP0FhnI294bicVmKdT'
#     sub_category_id = 'TqPufEzH9f9yuXQCa36S'
#     product_list = getProductsInfo(business_id,category_id,sub_category_id)
#     print(product_list)
#     categories = []
#     business_id,categories = getBusinessInfo('u2TBoGwM59RFU1u5wU7SBeEdZ6t2')
#     print('------------------------------')
#     print(categories)
#     return render_template('category/category.html', data = categories,product_list=product_list)

@mod.route("/<categoryId>/<subcategoryId>",methods=["GET", "POST"])
def get_category_details(categoryId,subcategoryId):
    product_list = getProductsInfo(session['business']['business_id'],categoryId,subcategoryId)
    categories = getBusinessCategories(session['business']['business_id'])
    print(categories)
    return render_template('category/products.html',categoryId=categoryId, subcategoryId=subcategoryId, categories = categories, product_list = product_list)

@mod.route("/add_category",methods=["POST"])
def add_category():
    user_id = addCategory(request.form['category'],session['business']['business_id'])
    if(user_id):
        return redirect('/home')
    else:
        return redirect("/")

@mod.route("/add_sub_category",methods=["POST"])
def add_sub_category():
    user_id = addSubCategory(request.form['categoryId'],request.form['subcategory'],session['business']['business_id'])
    if(user_id):
        return redirect('/home')
    else:
        return redirect("/")

@mod.route("/add_products",methods=["POST"])
def add_products():
    img = request.files.getlist("images")
    if addProducts(request.form['categoryId'],request.form['subcategoryId'],request.form['productname'],request.form['productdesc'],request.form['productprice'],session['business']['business_id'],img):
        flash("Product created","success")
        return redirect('/category/'+request.form['categoryId']+'/'+request.form['subcategoryId'])
    else:
        flash("Product not created","danger")
        return redirect('/category/'+request.form['categoryId']+'/'+request.form['subcategoryId'])

@mod.route("/get_category_name",methods=["POST"])
def get_category_name():
    x=request.get_json()['name']
    category = []
    for i in firestore_client.collection('businesses').where('category','==',x).get():
        business_id = i.id
        business_name = i.to_dict()['name'] 
        business_description = i.to_dict()['description']
        business_image =  i.to_dict()['image']
        category.append({'business_id':business_id,'business_name':business_name,'business_description':business_description,'business_image':business_image})
    return jsonify({'category':category})
    

