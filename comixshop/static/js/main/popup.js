$(document).ready(function(){
    var book = " ";
    var previous_book = " ";

    $("button").click(function(){
        book = $(this).attr("class");
        
        $(".info" + previous_book.toString()).hide();
        $(".info" + book.toString()).show();

        previous_book = book;
    });

    $(".info_close").click(function(){
        $(".info" + book.toString()).hide();
    });
});