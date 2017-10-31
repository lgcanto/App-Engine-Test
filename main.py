import webapp2

with open('forms.html', 'r') as myfile:
    form=myfile.read()

class MainPage(webapp2.RequestHandler):
    def write_form(self, message = ""):
        self.response.out.write(form % {"message": message})
    
    def get(self):
        self.write_form()
    
    def post(self):
        userDay = self.request.get('day')
        userMonth = self.request.get('month')
        userYear = self.request.get('year')
        if userDay.isdigit() and userMonth.isdigit() and userYear.isdigit():
            self.write_form("That's okay.")
        else:
            self.write_form("Invalid date.")

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)