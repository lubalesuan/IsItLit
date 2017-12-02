from flask import Flask, render_template
import random
app = Flask(__name__)

time_labels =['7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm']

@app.route('/')
def hello_world():
	return render_template('index.html',gym=True,mail=False)

@app.route('/gym')
def gym():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("gym.html",labels=time_labels,values=values)

@app.route('/mail')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("mail.html",labels=time_labels,values=values)

if __name__ == "__main__":
	app.run()
