/* DEFINE ELEMENTS */
/* Modal */
const modal = document.querySelector(".modal");

/* Buttons */
const modalBtn = document.querySelector(".btn-modal");
const modalClose = document.querySelector(".modal_close");

/* DEFINE FUNCTIONS */
/*Toggle modal*/
modalBtn.addEventListener("click", function () {
  modal.classList.toggle("hidden");
});
modalClose.addEventListener("click", function () {
  modal.classList.toggle("hidden");
});
