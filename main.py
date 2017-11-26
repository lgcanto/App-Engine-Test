import webapp2
import cgi
import string
import re

with open('welcome.html', 'r') as myfile:
    welcome=myfile.read()

with open('signup.html', 'r') as myfile:
    signup=myfile.read()

def escape_html(text):
    return cgi.escape(text, quote = True)

class Signup(webapp2.RequestHandler):
    def write_signup(self, username = "",
                           email = "",
                           username_error = "",
                           password_error = "",
                           verifypass_error = "",
                           email_error = ""):
        self.response.out.write(signup % {"user_username": username,
                                          "user_email": email,
                                          "username_error": username_error,
                                          "passsword_error": password_error,
                                          "verifypass_error": verifypass_error,
                                          "email_error": email_error})

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
            self.write_signup(userName, email, userError, passError, verifyError, emailError)

class Welcome(webapp2.RequestHandler):
    
    def write_welcome(self):
        self.response.out.write(welcome % {"user_username": self.request.get('username')})
    
    def get(self):
        self.write_welcome()

class Redirect(webapp2.RequestHandler):
    
    def get(self):
        self.redirect("/signup")

app = webapp2.WSGIApplication([
    ('/', Redirect),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)