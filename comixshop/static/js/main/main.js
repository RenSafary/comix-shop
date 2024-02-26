$(document).ready(function(){
    var screen_x = $(window).width();
    var screen_y = $(window).height();
    //alert("X = " + screen_x + " Y = " + screen_y);


    $(".manhwa").click(function(){
        $(this).animate({opacity: 0.7}, "fast");
        $(".manga").animate({opacity: 1.0});
        $(".manhua").animate({opacity: 1.0});
    });

    $(".manga").click(function(){
        $(this).animate({opacity: 0.7}, "fast");
        $(".manhwa").animate({opacity: 1.0});
        $(".manhua").animate({opacity: 1.0});
    });

    $(".manhua").click(function(){
        $(this).animate({opacity: 0.7}, "fast");
        $(".manhwa").animate({opacity: 1.0});
        $(".manga").animate({opacity: 1.0});
    });
});