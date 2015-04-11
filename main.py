import webapp2
from handler import MainHandler, AddQuestion, QuestionsHandler

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/questions', QuestionsHandler),
							   ('/add_question', AddQuestion)], debug=True)
