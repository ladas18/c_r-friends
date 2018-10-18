from flask import render_template, redirect, request
from cr_friends.config.mysqlconnection import connectToMySQL
from cr_friends.models.friend import Friend

friend = Friend()
class Friends():
    def index(self):
        result = friend.index()
        return render_template('index.html', friends = result)

class addFriends():
    def addFriends(self):
        new_friend_id = friend.addFriends()
        return redirect('/')
