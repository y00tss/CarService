
    document.addEventListener('DOMContentLoaded', function () {
        var orderButtons = document.querySelectorAll('.order-button');
        var successMessage = document.getElementById('success-message');

        orderButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                if (button.classList.contains('clicked')) {
                    return;  // Prevent multiple clicks
                }

                // Show the success message and animate it
                button.classList.add('clicked');
                successMessage.style.display = 'block';
                setTimeout(function () {
                    successMessage.style.display = 'none';
                }, 3000); // Display the message for 3 seconds
            });
        });
    });

