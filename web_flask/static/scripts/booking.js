const startDateInput = document.getElementById('start_date');
const endDateInput = document.getElementById('end_date');
const totalAmount = document.getElementById('total-amount');
const amountInput = document.getElementById('amount');
const pricePerDay = JSON.parse(document.getElementById('price-per-day').textContent);

function calculateAmount() {
    if (startDateInput.value && endDateInput.value) {
        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);
        const days = (endDate - startDate) / (1000 * 60 * 60 * 24);
        if (days > 0) {
            const total = pricePerDay * days;
            totalAmount.textContent = total.toFixed(2);
            amountInput.value = total.toFixed(2);
        } else {
            totalAmount.textContent = 0;
            amountInput.value = 0;
        }
    }
}

startDateInput.addEventListener('change', calculateAmount);
endDateInput.addEventListener('change', calculateAmount);

