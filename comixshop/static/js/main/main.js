$(document).ready(function(){
    $(".icon").click(function(){
        window.location.href = "/";
    });

    $(".name").click(function(){
        window.location.href = "/";
    });

    $(".products_redirect").click(function(){
        window.location.href = "/books/";
    });

    $(".find_form").submit(function(){ 
        if ($(".find").val() == ""){
            event.preventDefault();
        }
    });
});