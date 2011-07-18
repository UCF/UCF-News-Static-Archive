var addthis_config = {
	data_use_flash: false //This fixes an issue where addthis adds space to the
	                      //top of the page...addthis, more like addspace! HAHA
}

jQuery(window).load(function(){
	initQuickLinks();
	
	//Clears default value from input box on focus.
	jQuery('#q').focus(function(){
		if(jQuery(this).val() == 'Search UCF'){
			jQuery(this).val('');
		}
	});
	jQuery('#q').blur(function(){
		if(jQuery(this).val() == ''){
			jQuery(this).val('Search UCF');
		}
	});

	jQuery('#search_news').focus(function(){
		if(jQuery(this).val() == 'Search News Stories'){
			jQuery(this).val('');
		}
	});
	jQuery('#search_news').blur(function(){
		if(jQuery(this).val() == ''){
			jQuery(this).val('Search News Stories');
		}
	});
	
	
	$(".full_photo")
		.click(function() {
				window.open($(this).attr('id'), 'popup', "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, copyhistory=no, width=400, height=400");
		});
	
	$("h1 .rss")
		.click(function(){
			return addthis_open(this, 'feed', $(this).attr('href'));
		});
});

