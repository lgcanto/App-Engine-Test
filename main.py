import webapp2
import cgi
import string

with open('forms.html', 'r') as myfile:
    form=myfile.read()

def escape_html(text):
    return cgi.escape(text, quote = True)

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

inverse_rot13 = string.maketrans( 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm", 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

ToROT13 = True

class ROT13(webapp2.RequestHandler):
    
    def write_form(self, text = ""):
        self.response.out.write(form % {"user_text": text})

    def get(self):
        self.write_form()
        
    def post(self):
        text = str(self.request.get('text'))
        if ToROT13:
            text = string.translate(text, rot13)
            ToROT13  = False
        else:
            text = string.translate(text, inverse_rot13)
            ToROT13  = True
        
        self.write_form(escape_html(text))

app = webapp2.WSGIApplication([
    ('/', ROT13)
], debug=True)

# class MainPage(webapp2.RequestHandler):
#     def write_form(self, message = "", month = "", day = "", year = ""):
#         self.response.out.write(form % {"message": message,
#                                         "month": month,
#                                         "day": day,
#                                         "year": year})
    
#     def get(self):
#         self.write_form()
    
#     def post(self):
#         userMonth = escape_html(str(self.request.get('month')))
#         userDay = escape_html(str(self.request.get('day')))
#         userYear = escape_html(str(self.request.get('year')))
#         if not (userDay.isdigit() and userMonth.isdigit() and userYear.isdigit()):
#             self.write_form("Invalid date.", userMonth, userDay, userYear)
#         else:
#             self.redirect("/thanks")

# class Thanks(webapp2.RequestHandler):
#     def get(self):
#         self.response.out.write("Thank you for your submit.")

# app = webapp2.WSGIApplication([
#     ('/', MainPage),
#     ('/thanks', Thanks)
# ], debug=True)