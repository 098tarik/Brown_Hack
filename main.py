# Copyright 2016 Google Inc.
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
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import random
TEMPLATE = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True
)
class patient(ndb.Model):
    severity = ndb.StringProperty()
    condition = ndb.StringProperty()
    location = ndb.StringProperty() 
    
class CssiUser(ndb.Model):
 
  # user sign in datastore, this object stores user information
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  username = ndb.StringProperty()
  email = ndb.StringProperty()
  gender = ndb.StringProperty()
  location = ndb.StringProperty()


class Login(webapp2.RequestHandler):
    def get(self):
        error = self.request.get('error')
        content = TEMPLATE.get_template('Templates/login.html')        

#class LandingPage(webapp2.RequestHandler):

#class SignUp(webapp2.RequestHandler):
    


class MainPage(webapp2.RequestHandler):
    def get(self):
       content = TEMPLATE.get_template('Templates/help.html')
 
       self.response.write(content.render())
        
    def post(self):
        content = TEMPLATE.get_template('Templates/help.html')
        cssi_user= CssiUser(
        username=self.request.get('Username')
        )
        cssi_user.put()
        self.response.write(content.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login',Login)
], debug=True)
