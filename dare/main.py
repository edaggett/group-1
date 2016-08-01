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
from random import randint

env=jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
    def get(self):
       template=env.get_template("main.html")
       
       self.response.write(template.render())

class LogInHandler():
	def get(self):
		user = users.get_current_user()
		if user:
			greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
			(user.nickname(), users.create_logout_url('/')))
		else:
			greeting = ('<a href="%s">Sign in or register</a>.' %
			users.create_login_url('/'))

		self.response.out.write('<html><body>%s</body></html>' % greeting)

class DareHandler(webapp2.RequestHandler):
  def get(self):
    template=env.get_template("dare.html")
    dares={"dare1": "high five", "2" : "hug", "3": "smile"}
    self.response.write(template.render(dares))
  def get(self):
		template=env.get_template("dare.html")
		data = ["hug your mom", "give a high five to your legal guardian", "plant a flower", "wave at someone"]
		random_item = random.randint(0, len(data))
		the_dare = data[random_item]


		self.response.write(template.render(the_dare))


app = webapp2.WSGIApplication([
    ('/', MainHandler), ("/dare", DareHandler)










], debug=True)
