$(document).ready(function(){
    $(".icon").click(function(){
        window.location.href = "/";
    });

    $(".products redirect").click(function(){
        window.location.href = "/products/"; // it doesn't work because there are no padding parameters
    });

    $(".find_form").submit(function(){ // text is empty
        if ($(".find").text() == ""){
            alert($(".find").text());
        }
        event.preventDefault();

    });
});