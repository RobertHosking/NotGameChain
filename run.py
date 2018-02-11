from flask import Flask



app = Flask(__name__)

@app.route("/")
def index():
	print("this ran")
	return '<h1>Never</h1>'

app.run(debug=True, host="0.0.0.0", port=5000)
