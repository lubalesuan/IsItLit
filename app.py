from flask import Flask, render_template
import random
app = Flask(__name__)

time_labels =['7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm']
places_array = ['carlson_library', 'danforth_dining_hall', 'douglass_dining_hall',
				'georgen_athletic_center', 'gleason_library', 'mail_services', 
				'peets_coffee', 'q_and_a']

@app.route('/')
def hello_world():
	return render_template('index.html',gym=True,mail=False, place_names = places_array)

@app.route('/places/<string:name_place>')
def place(name_place):
	if name_place in places_array:
		values = [random.randint(0,20) for x in range(len(time_labels))]
		name_place = name_place.replace("_", " ")
		return render_template("places.html", labels = time_labels, values = values, pn = name_place)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
if __name__ == "__main__":
	app.run()
