const openButtons = document.querySelectorAll(".openPopup");
const closeButtons = document.querySelectorAll(".close");
const popups = document.querySelectorAll(".popup");
const body = document.body;

openButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
        popups[index].style.display = "block";
        body.style.overflow = "hidden";
    });
});

closeButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
        popups[index].style.display = "none";
        body.style.overflow = "auto";
    });
});

window.addEventListener("click", event => {
    popups.forEach(popup => {
        if (event.target === popup) {
            popup.style.display = "none";
            body.style.overflow = "auto";
        }
    });
});