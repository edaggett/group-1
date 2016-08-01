from google.appengine.ext import ndb

class Dares(ndb.Model):
	dare_number=IntegerProperty(required=True)
	dare=ndb.StringProperty(required=True)