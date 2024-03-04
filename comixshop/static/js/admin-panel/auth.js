$(document).ready(function(){
    $(".form").submit(function(){
        event.preventDefault()

        $.ajax({
            url: '/auth/',
            type: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                if (response.message == "fail"){
                    alert("Неверный логин или пароль.");
                }
                else{
                    window.location.href = "/books/";
                }
            },
            error: function(xhr, errmsg, err){
                console.log("Ошибка: " + xhr.status);
            }
        });
    });
});