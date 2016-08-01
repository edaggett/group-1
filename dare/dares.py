from google.appengine.ext import ndb

class Dares(ndb.Model):
	dare_number=ndb.IntegerProperty(required=True)
	dare=ndb.StringProperty(required=True)