function getCookie(c_name){
    if (document.cookie.length > 0){
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1){
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) 
                c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}


$('#login-button').on('click', function(e) {
    var uname = document.getElementById('form-username').value;
    var pass = document.getElementById('form-password').value;
    $(function () {
        $.ajaxSetup({
            // Initialise every AJAX request with CSRFToken
            // so no need to send it in every JSON request.
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
    });

    // var loading_screen = pleaseWait({
    //     // logo: "./images/pathgather.png",
    //     backgroundColor: '#f46d3b',
    //     loadingHtml: "<div class='spinner'><div class='rect1'></div><div class='rect2'></div><div class='rect3'></div><div class='rect4'></div><div class='rect5'></div></div>"
    // });

	$.ajax({
        type: 'POST',
        url: "/login",
        data : { 'uname': uname, 'pass': pass },
        success : function(json) {
            if(json=="OK"){
                $("#success").modal("show");
                window.location="/ShowSplash";
            }else{
                $("#failure").modal("show");
            }
        }
    })
}); 



