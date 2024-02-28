$(document).ready(function(){
    $(".redirect").click(function(){
        window.location.href = "/";
    });

    $(".logout").click(function(){
        window.location.href = "/logout/"
    });

    $(".add_book").click(function(){
        window.location.href = '/products/add/'
    });
});