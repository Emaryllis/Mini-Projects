import shelve, forms, login
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'a'
@app.route('/')
def redirectHome():
	return redirect(url_for('homePage'))
@app.route('/home')
def homePage():
	return render_template('home.html')
@app.route('/contactUs', methods=['GET', 'POST'])
def contactUsPage():
	contactForm = forms.createContactForm(request.form)
	if request.method == 'POST' and contactForm.validate():
		contactDict, contactDb = {}, shelve.open('contactUs.db', 'c')
		try:
			contactDict = contactDb['Contact']
		except:
			print('Error in retrieving Contact Database')
		contact = contactDict[contact.getId()] = forms.Contact(
			contactForm.firstName.data, contactForm.lastName.data, contactForm.email.data, contactForm.contactHelp.data)
		contactDb['Contact'], session['contactUsName'], session[
			'contactUsEmail'] = contactDict, f'{contact.getFirstName()} {contact.getLastName()}', contact.getEmail()
		contactDb.close()
		return redirect(url_for('thankYouPage'))
	return render_template('contactUs.html', contact=contactForm, request=request.method)
@app.route('/thankYou')
def thankYouPage():
	try:
		if type(session['contactUsName']) == str:
			return render_template('thankYou.html')
	except KeyError:
		return redirect(url_for('homePage'))


@app.route('/login')
def loginPage():
	return render_template('login.html')
@app.route('/register', methods=['GET', 'POST'])
def registerPage():
	print(type(request.path))
	registerForm = login.CreateRegisterForm(request.form)
	if request.method == 'POST' and registerForm.validate():
		RegisterDict, RegisterDb = {}, shelve.open('Users.db', 'c')
		try:
			RegisterDict = RegisterDb['Users']
		except:
			print('Error in retrieving Register Database')
		if registerForm.repPassword.data != registerForm.password.data:
			raise "Passwords do not match!"
		else:
			Register = RegisterDict[Register.getId()] = login.User(registerForm.email.data, registerForm.password.data)
		RegisterDb['Users'], session['UserEmail'], session['UserId'] = RegisterDict, Register.getEmail(),Register.getId()
		RegisterDb.close()
		return redirect(url_for('dashPage'))
	return render_template('register.html', register=registerForm, request=request.method)
@app.route('/FAQ')
def FAQPage(): return render_template('FAQ.html')
@app.errorhandler(404)
def page404(e):
	return render_template('404.html'), 404
@app.route(f'/{app.secret_key}')
def consolePage(): return render_template('console.html')
@app.route('/dashboard')
def dashPage(): 
	#Replace with home redirect after testing
	return render_template('dashboard.html',userId=session['userId'])if 'userId' in session else render_template('dashboard.html')
	
if __name__ == '__main__':
	app.run(debug=True, port=80)