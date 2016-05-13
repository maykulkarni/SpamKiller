$(document).ready(function(){
	var loading_screen = pleaseWait({
        // // logo: "./images/pathgather.png",
        backgroundColor: '#363636',
        loadingHtml: "<h2>Loading</h2><div class='spinner'><div class='rect1'></div><div class='rect2'></div><div class='rect3'></div><div class='rect4'></div><div class='rect5'></div></div>"
    });
    window.location="/landing_page"
});