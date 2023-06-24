let accordions = document.querySelectorAll(".accordion");

accordions.forEach((accordion) => {
  let accordionBtn = accordion.querySelector(".accordion-btn");

  accordionBtn.addEventListener("click", (e) => {
    e.preventDefault();
    accordion.classList.toggle("open");
  });
});
