$(document).ready(function(){
    $(".icon").click(function(){
        window.location.href = "/";
    });

    $(".name").click(function(){
        window.location.href = "/";
    });

    $(".products redirect").click(function(){
        window.location.href = "/books/"; // it doesn't work because there are no padding parameters
    });

    $(".find_form").submit(function(){ 
        if ($(".find").val() == ""){
            event.preventDefault();
        }
    });
});