// get current year
(function () {
  var year = new Date().getFullYear();
  document.querySelector("#currentYear").innerHTML = year;
})();

document.addEventListener("DOMContentLoaded", function () {
  const toastElList = [].slice.call(document.querySelectorAll(".toast"));
  toastElList.forEach(function (toastEl) {
    const toast = new bootstrap.Toast(toastEl);
    toast.show();
  });
});
