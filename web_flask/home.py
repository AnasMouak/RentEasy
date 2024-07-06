#!./venv/bin/python
'''starts a Flask web application'''
from flask import Flask, render_template, request, redirect, url_for, flash
from models import storage
from models.car_maker import CarMaker
from models.car_model import CarModel
from models.booking import Booking

# Initialize the Flask application
app = Flask(__name__, template_folder='templates')
app.secret_key = 'super_secret_key'

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

@app.route('/Cars/<car_maker_name>',)
def car_models(car_maker_name):
    car_maker = None
    car_models = []
    # Find the car maker by name
    for maker in storage.all(CarMaker).values():
        if maker.name.lower() == car_maker_name.lower():
            car_maker = maker
            car_models = maker.car_models
            break
    if not car_maker:
        return "Car maker not found", 404
    return render_template('car_models.html', car_maker=car_maker, car_models=car_models)

@app.route('/cars/<car_maker_name>/<car_model_name>/book', methods=['GET', 'POST'])
def book_car(car_maker_name, car_model_name):
    car_maker = None
    car_model = None
    
    # Find the car model by name within the specified car maker
    for maker in storage.all(CarMaker).values():
        if maker.name.lower() == car_maker_name.lower():
            car_maker = maker
            for model in maker.car_models:
                if model.name.lower() == car_model_name.lower():
                    car_model = model
                    break
            break
    
    if not car_model:
        return "Car model not found", 404
    
    if request.method == 'POST':
        # Get booking details from the form
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        city = request.form.get('city')
        country = request.form.get('country')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        amount = request.form.get('amount')
        
        # Create a new booking instance
        booking = Booking(name=name, 
                          email=email, 
                          phone=phone, 
                          address=address, 
                          city=city, 
                          country=country, 
                          start_date=start_date, 
                          end_date=end_date, 
                          car_model_id=car_model.id, 
                          amount=amount)

        # Save the booking to storage
        storage.new(booking)
        storage.save()
        flash('Booking successful!', 'success')
        return redirect(url_for('booking_success'))
    
    return render_template('booking.html', car_maker=car_maker, car_model=car_model)


@app.route('/booking_success')
def booking_success():
    return render_template('booking_success.html')

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

