// ******************** 
// init functions

var liqd = (function($, self) {

    self.bTT_initialised = false;


    // ******************** 
    // init backToTop Button

    self.init_backToTop = function() {

        if (self.bTT_initialised) return;
        if ($(window).innerWidth() < screen_sm) {

            var offset = 400;
            var duration = 300;

            $(window).on('scroll', function() {
                if ($(this).scrollTop() > offset) {
                    $('.back-to-top').fadeIn(duration);
                } else {
                    $('.back-to-top').fadeOut(duration);
                }
            });

            $('.back-to-top').on('click', function(event) {
                event.preventDefault();
                $('html, body').animate({scrollTop: 0}, duration);
                return false;
            });

            self.bTT_initialised = true;
        }

    };

    return self;

}(jQuery, liqd || {} ));