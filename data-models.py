from google.appengine.ext import db

class Question(db.Model):
	"""Defines each question """
	question = db.StringProperty(required = True)
	school = db.StringProperty(required = True)
	course = db.StringProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)	
	user = db.UserProperty(auto_current_user_add = True)
