from google.appengine.ext import ndb


class Points(ndb.Model):
	userpoints= ndb.IntegerProperty(default=0)

class Users(ndb.Model):
	username=ndb.StringProperty(required=True)
	points=ndb.StructuredProperty(Points)
	
class Memories(ndb.Model):
	pictures=ndb.BlobProperty(required=False)
	writing=ndb.StringProperty(required=False)
	owner=ndb.KeyProperty(Users)

