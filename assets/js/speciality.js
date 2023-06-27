let accordions = document.querySelectorAll(".accordion");

accordions.forEach((accordion) => {
  let accordionBtn = accordion.querySelector(".accordion-btn");

  accordionBtn.addEventListener("click", (e) => {
    e.preventDefault();
    accordion.classList.toggle("open");
  });
});

let popup = document.querySelector(".popup");
let closePopupBtn = document.querySelector(".close-popup");
let popupContent = document.querySelector(".popup-content");

window.onload = function () {
  popup.classList.toggle("show");
};

closePopupBtn.addEventListener("click", () => {
  popup.classList.toggle("show");
});
