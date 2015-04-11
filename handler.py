import webapp2
import jinja2
import os
from google.appengine.ext import db
from google.appengine.api import users
from data_models import Question, Answer

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment (loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self,template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

def render_str(template, **params):
	t = jinja_env.get_template(template)
	return t.render(params)

def question_key(question_parent='default'):
    """Constructs a Datastore key for a Question entity.

    We use question_parent as the key.
    """
    return db.Key.from_path('Question', question_parent)	

class MainHandler(Handler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.redirect('/questions')
		else:
			self.render("HomePage.html")	

logout_url = users.create_logout_url("/")

class QuestionsHandler(Handler):
	def get(self):
		# Checks for active Google account session
		user = users.get_current_user()

		if user:
			questions = Question.all().order('-created')
			school = self.request.get('school')
			course = self.request.get('course')
			if school:
				questions.filter("school =", school)
			if course:	
				questions.filter("course =", course)
			self.render("QuestionsHome.html", name = user.nickname(), questions = questions, logout_url = logout_url)
		else:
			self.redirect(users.create_login_url(self.request.uri))

class AddQuestion(Handler):
	def get(self):
		# Checks for active Google account session
		user = users.get_current_user()
		if user:
			self.render("add_question.html", name = user.nickname(), logout_url = logout_url)
		else:
			self.redirect(users.create_login_url(self.request.uri))

	def post(self):
		question = self.request.get('question')
		school = self.request.get('school')
		course = self.request.get('course')
		if question and school and course:
			question = Question(parent = question_key(question_parent = course), question = question, school = school, course = course)
			question.put()
			self.redirect('/')			

class UserPage(Handler):
	def get(self):
		user = users.get_current_user()
		u = User.all().filter('user_id =', user.user_id).get()
		if u:
			self.render("user_page.html", name = u.username)
		else:
			self.redirect("/edit_user_info")



