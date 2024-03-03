$(document).ready(function(){
    var book = undefined;
    var previous_book = undefined;

    $("button").click(function(){ // it doesn't work as i wanted to
        book = $(this).attr("class");
        previous_book = book;
        alert(previous_book);

        $(".info" + previous_book.toString()).hide();
        $(".info" + book.toString()).show();
    });

    $(".info_close").click(function(){
        $(".info" + book.toString()).hide();
    });
});