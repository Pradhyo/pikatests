import webapp2
from handler import MainHandler, AddQuestion, QuestionsHandler, MockHandler

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/questions', QuestionsHandler),
							   ('/mock', MockHandler),
							   ('/add_question', AddQuestion)], debug=True)
