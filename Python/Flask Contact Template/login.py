from wtforms import Form, StringField, TextAreaField, validators, PasswordField
from wtforms.fields import EmailField
from wtforms.widgets import PasswordInput


class User:
	def __init__(self, e, p):
		User.total = User.total+1 if hasattr(User, 'total') else 1
		self.userId, self.email, self.password = User.total, e, p
	def getId(self): return self.userId
	def getEmail(self): return self.email
	def getPassword(self): return self.password
	def setId(self, i): self.userId = i
	def setEmail(self, e): self.email = e
	def getPassword(self, c): self.password = p
	# Preferences
	def getFirstName(self):return self.firstName
	def getLastName(self):return self.lastName
	def setFirstName(self,f):self.firstName=f
	def setLastName(self,l):self.lastName=l
class CreateLoginForm(Form):
	email = EmailField('Email:', [validators.Email(), validators.DataRequired()])
	password = PasswordField('Password:', [validators.Length(min=8,max=30),validators.DataRequired()],widget=PasswordInput(hide_value=False))
class CreateRegisterForm(Form):
	email = EmailField('Email:', [validators.Email(), validators.DataRequired()])
	password = PasswordField('Password:', [validators.Length(min=8,max=30),validators.DataRequired()],widget=PasswordInput(hide_value=False))
	repPassword = PasswordField('Repeat Password:', [validators.Length(min=8,max=30),validators.DataRequired(),validators.EqualTo('password',message='Passwords do not match!')],widget=PasswordInput(hide_value=False))
