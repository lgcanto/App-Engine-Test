import webapp2
import os
import cgi
import string
import re
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def escape_html(text):
    return cgi.escape(text, quote = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Signup(Handler):
    def write_signup(self, **parameters):
        self.render('signup.html', **parameters)

    def get(self):
        self.write_signup()
        
    def post(self):
        usernameRegex = "^[a-zA-Z0-9_-]{3,20}$"
        passwordRegex = "^.{3,20}$"
        emailRegex = "^[\S]+@[\S]+.[\S]+$"

        userError = passError = verifyError = emailError = ""

        userName = escape_html(self.request.get('username'))
        email = escape_html(self.request.get('email'))
        password = escape_html(self.request.get('password'))
        confirmPassword = escape_html(self.request.get('verify'))
        
        emailMatch = re.match(emailRegex, email)
        passwordMatch = re.match(passwordRegex, password)
        usernameMatch = re.match(usernameRegex, userName)

        if (usernameMatch == None):
            userError = "Invalid Username."
        if (passwordMatch == None):
            passError = "Invalid password."
        if password != confirmPassword:
            verifyError = "Passwords didn't match."
        if (emailMatch == None) & (email != ""):
            emailError = "Invalid e-mail."
        
        if (userError == "") & (passError == "") & (verifyError == "") & (emailError == ""):
            self.redirect("/welcome?username=" + userName)
        else:
            self.write_signup(userName = userName,
                              email = email, 
                              userError = userError, 
                              passError = passError, 
                              verifyError = verifyError, 
                              emailError = emailError)

class Welcome(Handler):
    def write_welcome(self):
        self.render('welcome.html', userName = self.request.get('username'))
    
    def get(self):
        self.write_welcome()

class Fizzbuzz(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n=n)

class Lista(Handler):
    def get(self):
        itens = self.request.get_all('item')
        self.render('list.html', itens=itens)        

class Main(Handler):
    def get(self):
        self.render('base.html')

app = webapp2.WSGIApplication([
    ('/', Main),
    ('/signup', Signup),
    ('/welcome', Welcome),
    ('/fizzbuzz', Fizzbuzz),
    ('/list', Lista),
], debug=True)