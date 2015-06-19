$(document).ready(function() {
	if($(window).width()>768){
		$('.navbar .dropdown').hover(function(e) {
			var dropdown_width = $(this).outerWidth();
			var dropdown_menu = $(this).find('.dropdown-menu').first();
			var list_inline = $(dropdown_menu).find('.list-inline').first();
			var padding = parseInt($(list_inline).css('padding-left').replace("px", ""));
			var list_clone = list_inline.clone().css("visibility","hidden").appendTo($('body'));

			var width = 2*padding;

			$(list_clone).children().each(function(){
				width = width + $(this).width() + padding;
			});

			$(list_clone).remove();

			$(dropdown_menu).css({ "min-width": width });
			$(dropdown_menu).css({ "right":dropdown_width/2 -width/2});
			dropdown_menu.stop(true, true).delay(250).slideDown({duration: 100});

        }, function() {
            $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideUp({duration: 100});

        });

        $('.navbar .dropdown > a').click(function(){
            window.location.replace(this.href);
        });
    }

});