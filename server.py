from flask import Flask
from flask import render_template, request
from weather import getweather
import pickle
import json
import math

app = Flask(__name__)

def roundUp(num, points):
	tens = 10**points
	return math.ceil(num*tens)/tens
@app.route("/")
def index():
	w = getweather("DELHI", "cbbe618c3e4f5c2be6ca3e7c4efc8e0d")
	d,t = w.descntemp()
	t = roundUp(float(t), 1)
	return render_template("index.html", desc = d, temp = t)

@app.route("/notifications", methods=['GET'])
def noti():
	noti = request.args.get('noti')
	text = request.args.get('text')
	app = request.args.get('app')
	# icon = request.args.get('icon')
	notis = noti.split(",")
	texts = text.split(",")
	apps = app.split(",")
	# icons = icon.split(",")
	#print(noti, text, app)
	notifications = []
	for notiz,textz,appz in zip(notis,texts,apps):
		print(notiz,textz,appz)
		notifications.append((notiz,textz,appz))
	pickle.dump(notifications, open("notifications.pickle","wb"))
	return "okay"

@app.route("/getNoti")
def getNoti():
	notifications = pickle.load(open("notifications.pickle","rb"))
	json_noti = json.dumps(notifications)
	return json_noti

app.run(host="0.0.0.0", debug=True)