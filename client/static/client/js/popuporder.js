document.addEventListener('DOMContentLoaded', function () {
        var openPopupButton = document.querySelector('.openPopup');
        var closePopupButton = document.querySelector('.close');
        var popup = document.getElementById('orderPopup');

        openPopupButton.addEventListener('click', function () {
            popup.style.display = 'block';
        });

        closePopupButton.addEventListener('click', function () {
            popup.style.display = 'none';
        });
    });