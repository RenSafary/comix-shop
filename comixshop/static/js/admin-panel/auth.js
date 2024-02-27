$(document).ready(function(){
    $(".form").submit(function(){
        event.preventDefault()

        $.ajax({
            url: '/auth/',
            type: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                alert(response.message);
                if (response.message == "fail"){
                    alert("Неверный логин или пароль.");
                }
            },
            error: function(xhr, errmsg, err){
                console.log("Ошибка: " + xhr.status);
            }
        });
    });
});