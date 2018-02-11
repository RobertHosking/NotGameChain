from flask import Flask



app = Flask(__name__)

@app.route("/")
def index():
	print("this ran")
	return '<h1>Never</h1>'

if __name__=="__main__:":
	app.run(debug=True)
