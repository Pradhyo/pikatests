import webapp2
from handler import MainHandler, AddQuestion

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/add_question', AddQuestion)], debug=True)
