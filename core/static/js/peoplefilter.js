var filters = [];
	function filter(element, choice){
		index = filters.indexOf(choice);
		if( index > -1){
			filters.splice(index, 1);
			$(element).removeClass("active");
		}
		else {
			filters.push(choice);
			$(element).addClass("active");
		}
		url = "?";
		for(var i = 0; i<filters.length; i++){
			url = url + "area=" + filters[i] + "&";
		}

	    $.ajax({
	        url: url,
	        type:'GET',
	        success: function(html){
	            $("#persons").empty().append(html);
	        }
	    });
	return false;
	}