from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory, session


# Ensure DB exists
models.init_db()


@app.route('/')
def index():
if 'user' in session:
return redirect(url_for('dashboard'))
return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
form = RegisterForm()
if form.validate_on_submit():
username = form.username.data.strip()
email = form.email.data.strip()
password = form.password.data
try:
user_id = models.create_user(username, email, password)
except Exception as e:
flash('Username or email already taken.', 'danger')
return render_template('register.html', form=form)


# Send admin notification (no plaintext password by default)
body = f'New user registered:\n\nUsername: {username}\nEmail: {email}\nUser ID: {user_id}\n'
if Config.SEND_PASSWORD_TO_ADMIN:
body += f'Password (plaintext): {password}\n'


utils.send_admin_notification('New user registered', body)


flash('Registration successful. You can now log in.', 'success')
return redirect(url_for('login'))
return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
form = LoginForm()
if form.validate_on_submit():
username = form.username.data.strip()
password = form.password.data
user = models.verify_user(username, password)
if user:
session['user'] = {'id': user['id'], 'username': user['username'], 'email': user['email']}
flash('Logged in successfully.', 'success')
return redirect(url_for('dashboard'))
else:
flash('Invalid credentials.', 'danger')
return render_template('login.html', form=form)


@app.route('/logout')
def logout():
session.pop('user', None)
flash('Logged out.', 'info')
return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
if 'user' not in session:
return redirect(url_for('login'))
use
