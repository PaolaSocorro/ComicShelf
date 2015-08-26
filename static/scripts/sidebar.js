var menuLeft = document.getElementById('#smenu-s2'),
showLeftPush = document.getElementById('#showLeftPush'),
body = document.body;

showLeftPush.onclick = function(){
    menuLeft.toggleClass("smenu-open");
    body.toggleClass("smenu-left");
};