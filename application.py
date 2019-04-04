from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash, g
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User
from flask import session as login_session
from functools import wraps
import random
import string

import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog')
def showCatalog():
    categories = session.query(Categories).all()
    items = session.query(CategoryItem).order_by(
        CategoryItem.id.desc()).limit(10)
    return render_template('showCatalog.html', categories=categories, items=items)


'''
user_id temporary until login is added.
'''
@app.route('/catalog/newItem/', methods=['GET', 'POST'])
def addNewItem():
    if request.method == 'POST':
        newItem = CategoryItem(
            name=request.form['name'],
            description=request.form['description'],
            category_id=request.form['category_id'])
        session.add(newItem)
        session.commit()
        flash('New item added')
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newItem.html')


if __name__ == '__main__':
    app.secret_key = 'this-is-my-secret'
    app.run(host='0.0.0.0', port=8000)
