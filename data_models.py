from google.appengine.ext import db
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment (loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template, **params):
	t = jinja_env.get_template(template)
	return t.render(params)

class Question(db.Model):
	"""Defines each question """
	question = db.StringProperty(required = True)
	school = db.StringProperty()
	course = db.StringProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)	
	user = db.UserProperty(auto_current_user_add = True)

	def render_question(self):
		#Since we are passing as html, convert new lines to <br> to render new lines properly
		self._render_text = self.question.replace('\n', '<br>')
		return render_str("question.html", q = self)

class Answer(db.Model):
	"""Defines properties of an answer """
	answer = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)	
	user = db.UserProperty(auto_current_user_add = True)

class User(db.Model):
	"""Defines properties of User model """
	user_id = db.StringProperty(required = True)
	username = db.StringProperty(required = True)
	email = db.EmailProperty(required = True)
	department = db.StringProperty(required = True)
	rating = db.IntegerProperty()

class Course(db.Model):
	course_id = db.StringProperty(required = True)
	course_name = db.StringProperty()




