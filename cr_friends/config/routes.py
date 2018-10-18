from flask import render_template, redirect, request
from cr_friends import app
from cr_friends.config.mysqlconnection import connectToMySQL
from cr_friends.controllers.friends import Friends
friends = Friends()
@app.route('/')
def index():
    return friends.index()

@app.route('/process', methods=['POST'])
def addFriend():
    return friends.addFriends()
