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
    categories = session.query(Categories).order_by(asc(Categories.name))
    return render_template('showCatalog.html', categories=categories)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
