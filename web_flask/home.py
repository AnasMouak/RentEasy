#!./venv/bin/python
'''starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.car_maker import CarMaker
from models.car_model import CarModel

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

@app.route('/Cars/<car_maker_name>')
def car_models(car_maker_name):
    car_maker = None
    car_models = []
    for maker in storage.all(CarMaker).values():
        if maker.name.lower() == car_maker_name.lower():
            car_maker = maker
            car_models = maker.car_models
            break
    if not car_maker:
        return "Car maker not found", 404
    return render_template('car_models.html', car_maker=car_maker, car_models=car_models)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

