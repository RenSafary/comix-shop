$(document).ready(function(){
    $(".search").click(function(){
        $(".search-bar").show();
        $(".display").animate({opacity: 0.3});
    });

    $(".close").click(function(){
        $(".search-bar").hide();
        $(".display").animate({opacity: 1.0});
    });
});