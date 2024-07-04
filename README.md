
# RentEasy

![RentEasy Logo](images/logo.png "RentEasy Logo")

RentEasy is a user-friendly car rental website that allows you to easily rent cars for your travel needs. Whether you're planning a road trip, a business trip, or simply need a temporary vehicle, RentEasy has got you covered.

## installation

- Clone the repository:

```bash
$ git clone https://github.com/AnasMouak/RentEasy.git
$ cd RentEasy
```

## Usage

1. Set up a virtual environment (optional but recommended):

```bash
$ python -m venv venv
$ source venv/bin/activate
```

2. Install libraries:
```bash
$ pip install SQLAlchemy
$ pip install Flask
.
.
```

3. Configure Database:
```bash
$ sudo mysql -u root -p
MariaDB [(none)]> CREATE DATABASE IF NOT EXISTS renteasy_dev_db;
.
MariaDB [(none)]> CREATE USER IF NOT EXISTS 'renteasy_dev'@'localhost' IDENTIFIED BY 'your_password';
.
MariaDB [(none)]> GRANT ALL PRIVILEGES ON renteasy_dev_db.* TO 'renteasy_dev'@'localhost';
.
MariaDB [(none)]> GRANT SELECT ON performance_schema.* TO 'renteasy_dev'@'localhost';
.
```

4. Start the Flask development server:

```bash
$ RENTEASY_MYSQL_USER=renteasy_dev RENTEASY_MYSQL_PWD=your_password RENTEASY_MYSQL_HOST=localhost RENTEASY_MYSQL_DB=renteasy_dev_db RENTEASY_TYPE_STORAGE=db python3 -m web_flask.home
.
```



## Features

- **Wide Selection of Cars**: Choose from a diverse range of cars, including sedans, SUVs, luxury vehicles, and more.
- **Easy Booking Process**: Our intuitive booking system makes it simple to reserve a car in just a few clicks.
- **Flexible Rental Options**: Rent a car for a few hours, a day, a week, or even longer, depending on your needs.
- **Transparent Pricing**: We provide clear and upfront pricing, so you know exactly what you're paying for.
- **Convenient Pickup and Drop-off**: Select a convenient location to pick up and drop off your rental car.
- **24/7 Customer Support**: Our dedicated customer support team is available round the clock to assist you with any queries or concerns.

## Getting Started

To get started with RentEasy, follow these steps:

1. Visit our website at [www.renteasy.com](https://www.renteasy.com).
2. Sign up for an account or log in if you already have one.
3. Enter your desired pickup location, dates, and times.
4. Browse through the available cars and select the one that suits your needs.
5. Review the rental details and pricing.
6. Confirm your booking and make the payment.
7. Arrive at the designated pickup location at the scheduled time to collect your rental car.
8. Enjoy your journey!


## Technologies Used
RentEasy is developed using the following technologies:

- **Front-end Development**:
    - HTML
    - CSS
    - Jinja

- **Back-end Development**:
    - python
    - Flask
    - SQLAlchemy
    

- **Authentication and Authorization**:
    

- **Database**:
    - MariaDB
    

- **Payment Integration**:

- **Deployment**:
    
- **Version Control**:
    - Git

- **Other Tools and Libraries**:
    
## Contributing

    Anas Mouak

By utilizing these technologies, RentEasy provides a seamless and efficient car rental experience for its users.



