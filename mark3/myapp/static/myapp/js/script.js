var modal = document.getElementById('myModal');
var btn = document.getElementById("myBtn");
var span = document.getElementById("close");
var menu = document.getElementsByClassName("menu_n")
var ava = document.getElementById("nbt");
var m = document.getElementById("m");
btn.onclick = function() {

    m.style.right = 0;
    }
// Обрабатываем событие клика на элементе:
/*menu.addEventListener('click', () => {
  element.classList.toggle('element-final')
  element.classList.toggle('element-initial')
})*/
span.onclick = function() {modal.style.display = "none";}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";    }
}
menu.onclick =function(){
    if (event.target == menu) {
       m.style.right = -750;    }
}

function vidget(){
 modal.style.display = "block";}
function but() {
alert('Вы нажали на кнопку!');
m.style.right = -750;
}
