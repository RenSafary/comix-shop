$(document).ready(function(){
    for (let i = 0; i <= 10; i++){
        $(".book" + i.toString()).click(function(){
            $(".book" + i.toString()).show();
        });
    };
    $(".book2").click(function(){
        $(".info2").show();
    });

    $(".info_close").click(function(){ // если сисадмин добавит книгу, то список for уже будет неточен
        $(".info").hide();
    });
});