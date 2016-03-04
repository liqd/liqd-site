

// ******************** 
// Variables

var screen_xs = 480;
var screen_xs_max = screen_xs-1;
var screen_sm = 768;
var screen_sm_max = screen_sm-1;


// ******************** 
// slick slider init

$(document).ready(function(){
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
});


// ******************** 
// Language selector mobile

$('#select-lang-mobile').change(function(e)
{
    var selectedVal = $('#select-lang-mobile option:selected').val();
    if (selectedVal != "none") 
    {    
        var chunks = window.location.href.split('/');
        if (chunks[3] != selectedVal)
        {
            chunks[3] = selectedVal;
            window.location.href = chunks.join('/');
        }
        else
        {
            $('.navbar-toggle').click();
        }
    }

});