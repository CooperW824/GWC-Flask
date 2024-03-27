from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
		return 'Hello, World!'

@app.route('/hello')
def hello():
		return 'Hello GWC!'

@app.route('/<string:name>')
def hello_name(name):
		return f'Hello, {name}!'

def login(username, password):
		# TODO: Replace to use AWS COGNITO
		if username == 'admin' and password == 'password':
				return 'Login successful'
		else:
				return 'Login failed'

@app.route('/login', methods=['GET', 'POST'])
def test():
		if request.method == 'POST':
				data = request.get_data(as_text=True)
				data = data.split('&')
				username = data[0].split('=')[1]
				password = data[1].split('=')[1]
				return login(username, password)
		else:
				return render_template('login.html')
		