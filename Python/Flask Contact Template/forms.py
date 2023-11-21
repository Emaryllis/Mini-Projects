from wtforms import Form, StringField, TextAreaField, validators
from wtforms.fields import EmailField
class createContactForm(Form):
	firstName = StringField('First Name:', [validators.Length(min=1, max=150), validators.DataRequired()])
	lastName = StringField('Last Name:', [validators.Length(min=1, max=150), validators.DataRequired()])
	email = EmailField('Email:', [validators.Email(), validators.DataRequired()])
	contactHelp = TextAreaField('Message:', [validators.DataRequired()])
class Contact:
	def __init__(self,f,l,e,h):
		Contact.total=Contact.total+1 if hasattr(Contact, 'total') else 1
		self.contactId,self.firstName,self.lastName,self.email,self.contactHelp=Contact.total,f,l,e,h
	def getId(self):return self.contactId
	def getFirstName(self):return self.firstName
	def getLastName(self):return self.lastName
	def getEmail(self):return self.email
	def getContactHelp(self):return self.contactHelp
	def setId(self,i):self.contactId=i
	def setFirstName(self,f):self.firstName=f
	def setLastName(self,l):self.lastName=l
	def setEmail(self,e):self.email=e
	def getContactHelp(self,c):self.contactHelp=c