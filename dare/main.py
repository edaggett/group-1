#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.appengine.api import users
import webapp2
import jinja2
import random
import logging
from dares import Dares
from users import DareUsers
from users import Memories

from google.appengine.ext import ndb

env=jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

def findUser (user):
    find_dare_users=DareUsers.query().filter(DareUsers.user_id==user.user_id()).get()
    if find_dare_users==None:
        
        current_user=users.get_current_user()
        find_dare_users=DareUsers(user_id=current_user.user_id())
        find_dare_users.put()
    return find_dare_users



class Dares(ndb.Model):
    dare_number=ndb.IntegerProperty(required=False)
    dare=ndb.StringProperty(required=True, indexed=True)


class MainHandler(webapp2.RequestHandler):

    def get(self):
        template=env.get_template("main.html")
       
        user = users.get_current_user()
        
        if user:
            greeting = ('text-align: right, Welcome, %s! (<a href="%s">sign out</a>)' %
            (user.nickname(), users.create_logout_url('/')))
           # data["signed_in"]=True
        else:
            greeting = ('text-align: right, <a href="%s">Sign in or register</a>.' %
            users.create_login_url('/'))
            
            #data["signed_in"]=False

        data = {"LogIn" : greeting}
        

        self.response.write(template.render(data))



class DareHandler(webapp2.RequestHandler):
	def get(self):
	   template=env.get_template("dare.html")
		
	   dare_query=Dares.query()
	   dare_results=dare_query.fetch()
	   dare_result=dare_results[random.randint(0,len (dare_results)-1)]

	   dare={}
	   dare["number"]=dare_result.dare_number
	   dare["dare"]=dare_result.dare
	   self.response.write(template.render(dare))

class UserDare(webapp2.RequestHandler):
    def post(self):
        user_dare=self.request.get("daredare")
        d=Dares(dare=user_dare)
        d.put()
        template=env.get_template("main.html")
        self.response.write(template.render())

class DareCompleted (webapp2.RequestHandler):
    def post (self):
        if (self.request.get("completed_dare"))=="True":
             user=users.get_current_user()
             dare_completed_user=findUser(user)
             dare_completed_user.points+=1
             dare_completed_user.put()
        self.redirect("/")


        
app = webapp2.WSGIApplication([
('/userdare', UserDare),
     ("/dare", DareHandler), ('/', MainHandler), ("/darecompleted", DareCompleted)], debug=True)
