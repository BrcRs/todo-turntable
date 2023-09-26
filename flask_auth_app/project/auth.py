from flask import Blueprint, render_template, redirect, url_for
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    """
    For the sign-up function, you will take the data the user submits to the form 
    and add it to the database. You will need to make sure a user with the same 
    email address does not already exist in the database. If it does not exist, then 
    you need to make sure you hash the password before placing it into the database.
    """
    # TODO
    # code to validate and add user to database
    ## Storing passwords in plaintext is considered a poor security practice. 
    ## You will generally want a complex hashing algorithm and salt to keep passwords secure.
    return redirect(url_for('auth.login'))
@auth.route('/logout')
def logout():
    return "Logout"