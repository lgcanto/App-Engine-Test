import webapp2

form = """

<div>Please, insert your birth date:</div>
<form method="post">
    <label>
        Month
        <input type="text" name="month" > 
    </label>
    <br>
    <label>
        Day 
        <input type="text" name="day" >
    </label>
    <br>
    <label> 
        Year
        <input type="text" name="year" >
    </label>
    <br>
    <div style="color: red;">%(message)s</div>
<input type="submit" value="Submit">
</form>

"""
# form = 'forms.html'

class MainPage(webapp2.RequestHandler):
    def write_form(self, message = ""):
        self.response.out.write(form % {"message": message})
    
    def get(self):
        self.write_form()
    
    def post(self):
        #self.response.headers['Content-Type'] = 'text/plain'
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
