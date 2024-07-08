#!./venv/bin/python
'''starts a Flask web application'''
from flask import Flask, render_template, request, redirect, url_for, flash
from models import storage
from datetime import datetime, date
from models.car_maker import CarMaker
from models.car_model import CarModel
from models.booking import Booking
from models.contact import Contact

# Initialize the Flask application
app = Flask(__name__, template_folder='templates')
app.secret_key = 'super_secret_key'

# Custom Jinja2 filter
def to_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

# Register the custom filter with Flask's Jinja environment
app.jinja_env.filters['to_date'] = to_date


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
    '''returns a cars maker page'''
    car_makers = storage.all(CarMaker).values()
    return render_template('cars.html', car_makers=car_makers)


@app.route('/Cars/<car_maker_name>', strict_slashes=False)
def car_models(car_maker_name):
    '''returns a car models page'''
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

    return render_template('car_models.html', car_maker=car_maker,
                           car_models=car_models)


@app.route('/Contact', strict_slashes=False, methods=['POST'])
def contact_form():
    '''returns a contact page'''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        contact = Contact(name=name, email=email, message=message)
        storage.new(contact)
        storage.save()

        if not name or not email or not message:
            flash('Please fill out all fields', 'danger')
        else:
            flash('Message sent!', 'success')
        return redirect(url_for('contact_success'))
    
    return render_template('contact.html')


@app.route('/contact_success')
def contact_success():
    """Display a contact success page."""
    return render_template('contact_success.html')


def calculate_days(start_date, end_date):
    '''returns the number of days between two dates'''
    start = to_date(start_date)
    end = to_date(end_date)
    return (end - start).days


@app.route('/search', strict_slashes=False, methods=['GET'])
def search():
    '''returns a search page'''
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    days = calculate_days(start_date, end_date)

    if not start_date or not end_date:
        return redirect(url_for('home'))

    start_date_dt = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d').date()

    # Find all bookings that conflict with the selected dates
    booked_cars_ids = [
        booking.car_model_id for booking in storage.all(Booking).values() if (
            (booking.start_date <= start_date_dt <= booking.end_date) or
            (booking.start_date <= end_date_dt <= booking.end_date) or
            (start_date_dt <= booking.start_date and end_date_dt >= 
             booking.end_date)
        )
    ]

    # Find all car models that are not booked during the selected dates
    available_cars = [car for car in storage.all(CarModel).values()
                      if car.id not in booked_cars_ids]
    return render_template('search_results.html', available_cars=available_cars,
                           start_date=start_date, end_date=end_date, days=days)


@app.route('/search/<car_maker_name>/<car_model_name>/book', methods=['GET','POST'])
def book_search(car_maker_name, car_model_name):
    '''returns a booking page'''
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
    
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    days = calculate_days(start_date, end_date)

    if request.method == 'POST':
        # Get booking details from the form
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        city = request.form.get('city')
        country = request.form.get('country')
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
    
    return render_template('booking.html', car_maker=car_maker,
                           car_model=car_model, start_date=start_date,
                           end_date=end_date, days=days)


@app.route('/booking_success')
def booking_success():
    """Display a booking success page."""
    return render_template('booking_success.html')


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")