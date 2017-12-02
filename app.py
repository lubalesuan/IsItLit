from flask import Flask, render_template
import random
app = Flask(__name__)

time_labels =['7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm']

@app.route('/')
def hello_world():
	return render_template('index.html',gym=True,mail=False)

@app.route('/georgen_athletic_center')
def gym():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("georgen_athletic_center.html",labels=time_labels,values=values)

@app.route('/mailing_services')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("mailing_services.html",labels=time_labels,values=values)

@app.route('/douglass_dining_hall')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("douglass_dining_hall.html",labels=time_labels,values=values)

@app.route('/danforth_dining_hall')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("danforth_dining_hall.html",labels=time_labels,values=values)

@app.route('/hillside')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("hillside.html",labels=time_labels,values=values)

@app.route('/peetes_coffee')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("peetes_coffee.html",labels=time_labels,values=values)

@app.route('/gleason_library')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("gleason_library.html",labels=time_labels,values=values)

@app.route('/q_and_a')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("q_and_a.html",labels=time_labels,values=values)

@app.route('/carlson_library')
def mail():
	values = [random.randint(0,20) for x in range(len(time_labels))]
	return render_template("carlson_library.html",labels=time_labels,values=values)

if __name__ == "__main__":
	app.run()
