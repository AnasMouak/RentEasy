
document.addEventListener('DOMContentLoaded', function() {
    const pricePerDay = parseFloat(document.getElementById('price-per-day').innerText);
    const startDate = new Date(document.getElementById('start-date').innerText);
    const endDate = new Date(document.getElementById('end-date').innerText);
    const totalDays = (endDate - startDate) / (1000 * 60 * 60 * 24);
    const totalAmount = pricePerDay * totalDays;

    document.getElementById('total-amount').innerText = totalAmount.toFixed(2);
    document.getElementById('amount').value = totalAmount.toFixed(2);

    paypal.Buttons({
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: totalAmount.toFixed(2)
                    }
                }]
            });
        },
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {
                alert('Transaction completed by ' + details.payer.name.given_name);
                document.getElementById('booking-form').submit();
            });
        }
    }).render('#paypal-button-container');

    document.getElementById('book-button').addEventListener('click', function(e) {
        e.preventDefault();

        // Validate required fields
        const requiredFields = ['name', 'email', 'phone', 'address', 'city', 'country'];
        let allFieldsFilled = true;
        
        for (let field of requiredFields) {
            const inputElement = document.getElementById(field);
            if (inputElement.value.trim() === '') {
                allFieldsFilled = false;
                inputElement.classList.add('is-invalid');
            } else {
                inputElement.classList.remove('is-invalid');
            }
        }
        
        if (!allFieldsFilled) {
            alert('Please fill out all required fields.');
            return;
        }

        e.target.style.display = 'none';
        document.getElementById('paypal-button-container').style.display = 'block';
    });
});