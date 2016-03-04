

// ******************** 
// Variables

var screen_xs = 480;
var screen_sm = 768;
var screen_xs_max = screen_sm-1;



var liqd = (function($, self) {


    self.phone = ($(window).innerWidth() > screen_xs_max) ? false : true;


    // ******************** 
    // init slick slider

    self.init_slickSlider = function() {

        $('.block-carousel').slick({
            arrows: false,
            accessibility: true,
            dots: false,
            slidesToShow: 4,
            responsive: [
                {
                    breakpoint: screen_xs,
                    settings: {
                        centerMode: true,
                        slidesToShow: 1,
                        slidesToScroll: 1,
                        swipe: true,
                    }
                }
            ],
        });

    };


    return self;

}(jQuery, liqd || {} ));


// ******************** 
// document ready

$(document).ready(function() {
    liqd.init_backToTop();
    liqd.init_slickSlider();
});


// ******************** 
// check for orientation change
// remove backToTop layout switches from mobile to desktop (and restore)

$(window).smartresize(function(){

    if (liqd.phone && $(window).innerWidth() > screen_xs_max) {
        // $(window).off('scroll');
        // $('.back-to-top').fadeOut();
        // liqd.bTT_initialised = false;
        // liqd.phone = false;
        // liqd.init_slickSlider();
        window.location.href = window.location.href;

    }

    if (!liqd.phone && $(window).innerWidth() < screen_sm) {
        liqd.phone = true;
        liqd.init_backToTop();
        //window.location.href = window.location.href;
    }

});