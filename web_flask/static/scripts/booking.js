const startDateInput = document.getElementById('start_date');
const endDateInput = document.getElementById('end_date');
const totalAmount = document.getElementById('total-amount');
const amountInput = document.getElementById('amount');
const pricePerDay = parseFloat(document.getElementById('price-per-day').textContent);
const bookButton = document.getElementById('book-button');
const paypalContainer = document.getElementById('paypal-button-container');

console.log("Script loaded");

function calculateAmount() {
    console.log("Calculating amount...");
    if (startDateInput.value && endDateInput.value) {
        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);
        const days = (endDate - startDate) / (1000 * 60 * 60 * 24);
        if (days > 0) {
            const total = pricePerDay * days;
            totalAmount.textContent = total.toFixed(2);
            amountInput.value = total.toFixed(2);
        } else {
            totalAmount.textContent = '0';
            amountInput.value = '0';
        }
    }
}

startDateInput.addEventListener('change', calculateAmount);
endDateInput.addEventListener('change', calculateAmount);

bookButton.addEventListener('click', function(event) {
    event.preventDefault();
    console.log("Book button clicked");
    
    // Hide the book button and show PayPal container
    bookButton.style.display = 'none';
    paypalContainer.style.display = 'block';
    
    paypal.Buttons({
        createOrder: function(data, actions) {
            console.log("Creating order");
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: amountInput.value
                    }
                }]
            });
        },
        onApprove: function(data, actions) {
            console.log("Order approved");
            return actions.order.capture().then(function(details) {
                console.log('Transaction completed by ' + details.payer.name.given_name);
                alert('Transaction completed by ' + details.payer.name.given_name);
                
                // Submit the original booking form
                document.getElementById('booking-form').submit();
            });
        }
    }).render('#paypal-button-container');
});