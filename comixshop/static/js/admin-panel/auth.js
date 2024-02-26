$(document).ready(function(){
    $(".form").submit(function(){
        event.preventDefault()

        $.ajax({
            url: '/adm/',
            type: 'POST',
            data: $(this).serialize(),
            dataType: 'json',
            success: function(response){
                alert(response.message);
                if (response.message == "fail"){
                    alert("Неверный логин или пароль.");
                }
                if (response.message == undefined){
                    alert("hi");
                }
            },
            error: function(xhr, errmsg, err){
                console.log("Ошибка: " + xhr.status);
            }
        });
    });
});