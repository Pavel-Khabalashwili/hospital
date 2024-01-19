let showStatus  = document.querySelectorAll(".status-btn");//  Отслеживание кнопки "показать статус"
let statusBlock = document.querySelectorAll(".applications__status-info");// Отслеживания блока "статус"

showStatus.forEach(function(element, index){
    element.addEventListener("click", function(element){
        statusBlock[index].classList.toggle("show-status");
    });
});