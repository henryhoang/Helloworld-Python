#app.py
#!/usr/bin/env python


from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
	return '<h1> Hey Docker from j2 Global!</h1>'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
