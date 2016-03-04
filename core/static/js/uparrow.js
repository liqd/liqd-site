$(document).ready(function() {

    var offset = 400;
    var duration = 300;
    if($(window).width()<screen_sm_max){
        console.log("setup backtotop");
        $(window).scroll(function() {
            console.log($(this).scrollTop());
            if ($(this).scrollTop() > offset) {
                $('.back-to-top').fadeIn(duration);
            } else {
                $('.back-to-top').fadeOut(duration);
            }
        });

        $('.back-to-top').click(function(event) {
            event.preventDefault();
            $('html, body').animate({scrollTop: 0}, duration);
            return false;
        })
    };
});