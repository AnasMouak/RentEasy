#!./venv/bin/python
'''starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.car_maker import CarMaker

app = Flask(__name__, template_folder='templates')

@app.route('/', strict_slashes=False)
def home():
    '''returns a home page'''
    return render_template('home.html')

@app.route('/Contact', strict_slashes=False)
def contact():
    '''returns a contact page'''
    return render_template('contact.html')

@app.route('/Cars', strict_slashes=False)
def cars():
    car_makers = storage.all(CarMaker).values()
    return render_template('cars.html', car_makers=car_makers)



@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

