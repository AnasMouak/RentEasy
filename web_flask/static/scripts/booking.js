// Get references to the start date input, end date input, total amount display, amount input, and price per day
const startDateInput = document.getElementById('start_date');
const endDateInput = document.getElementById('end_date');
const totalAmount = document.getElementById('total-amount');
const amountInput = document.getElementById('amount');
const pricePerDay = JSON.parse(document.getElementById('price-per-day').textContent);

// Calculate the total amount based on the start date, end date, and price per day
function calculateAmount() {
    // Check if both the start date and end date have been selected
    if (startDateInput.value && endDateInput.value) {
        // Convert input values to Date objects
        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);
        // Calculate the number of days between the start date and end date
        const days = (endDate - startDate) / (1000 * 60 * 60 * 24);
        // If the number of days is positive, calculate the total amount
        if (days > 0) {
            const total = pricePerDay * days;
            // Update the total amount display and the hidden amount input
            totalAmount.textContent = total.toFixed(2);
            amountInput.value = total.toFixed(2);
        } else {
            // If the end date is before or the same as the start date, set the total amount to 0
            totalAmount.textContent = 0;
            amountInput.value = 0;
        }
    }
}

// Add event listeners to the start and end date inputs to recalculate the amount when the dates change
startDateInput.addEventListener('change', calculateAmount);
endDateInput.addEventListener('change', calculateAmount);

