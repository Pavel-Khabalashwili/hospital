// БУРГЕР МЕНЮ, АНИМАЦИЯ -------------------
let burger = document.querySelector(".burger");
let menu = document.querySelector(".header-nav");


burger.addEventListener("click", function(){
  burger.classList.toggle("burger_active");
  menu.classList.toggle("header__nav_brg-anim");
  document.body.classList.toggle("stop-scroll");
});