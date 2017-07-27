var main = function() {
	/*make menu appear*/
	$('.33637659345a626778746e616d6566597975453d').click(function(){
		if($('.3463335836413d3d').hasClass("3139546331773d3d")){
			$('.3463335836413d3d').animate({
				left: "0px"
			}, 400);
			$('.3463335836413d3d').removeClass("3139546331773d3d");
			$('.3463335836413d3d').addClass("34396a4f34633758");
		}
		else {
			$('.3463335836413d3d').animate({
				left: "-285px"
			}, 400);
			$('.3463335836413d3d').removeClass("34396a4f34633758");
			$('.3463335836413d3d').addClass("3139546331773d3d");
		}
	});
	width_timeline = $('.364e4857324e58637a394353342d6e56792d4c643564445a').width();
	console.log(width_timeline);
	if(width_timeline<= 1000){
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.item').addClass('33647a4f344e7a6777746652');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.timeline').addClass('32397259364e6e6d7a737a5235513d3d').addClass('smalltime');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.33647a4f34413d3dsmall').removeClass('33647a4f34413d3d');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.smalltime').removeClass('32397259364e6b3d').removeClass('timeline');
		}
		else {
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.33647a4f34413d3dsmall').addClass('33647a4f34413d3d');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.smalltime').addClass('32397259364e6b3d').addClass('timeline');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.item').removeClass('33647a4f344e7a6777746652');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.timeline').removeClass('32397259364e6e6d7a737a5235513d3d').removeClass('smalltime');
		}
	$(window).resize(function(){
		width_timeline = $('.364e4857324e58637a394353342d6e56792d4c643564445a').width();
		console.log(width_timeline);
		if(width_timeline<= 1000){
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.item').addClass('33647a4f344e7a6777746652');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.timeline').addClass('32397259364e6e6d7a737a5235513d3d').addClass('smalltime');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.33647a4f34413d3dsmall').removeClass('33647a4f34413d3d');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.smalltime').removeClass('32397259364e6b3d').removeClass('timeline');
		}
		else {
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.33647a4f34413d3dsmall').addClass('33647a4f34413d3d');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.smalltime').addClass('32397259364e6b3d').addClass('timeline');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.item').removeClass('33647a4f344e7a6777746652');
			$('.364e4857324e58637a394353342d6e56792d4c643564445a').find('.timeline').removeClass('32397259364e6e6d7a737a5235513d3d').removeClass('smalltime');
		}
	});
	relativesize = $('.313966583538725731513d3d').width()*0.03;
		if (relativesize>=36) {
			relativesize = 36;
		}
	console.log(relativesize);
	$('.3139665835387257315975543375484a3074383d').css('font-size', relativesize);
	$(window).resize(function(){
		relativesize = $('.313966583538725731513d3d').width()*0.03;
		if (relativesize>=36) {
			relativesize = 36;
		}
		console.log(relativesize);
		$('.3139665835387257315975543375484a3074383d').css('font-size', relativesize);
	});
	$('.364e4857324e58637a394346703933637a75413d').click(function(){
		if($(this).hasClass('313933623563376831513d3d')){
			$('.33647a4f34413d3d').removeClass('313933623563376831513d3d');
			$('.364e4857324e58637a394346703933637a75434a6f635851324e7a6d30646e6e30754c50').hide('200');
		}
		else{
			$('.33647a4f34413d3d').removeClass('313933623563376831513d3d');
			$('.364e4857324e58637a394346703933637a75434a6f635851324e7a6d30646e6e30754c50').hide('200');
			$(this).addClass('313933623563376831513d3d');
			$(this).children('.324d33633174766330645f4f364f493d').show('200');
		}
	});
	$('.3539584b3339586e79746a4b6d614c5233646a573573374d3065553d').click(function(){
		if($(this).hasClass('313933623563376831513d3d')){
			$('.33647a4f344e7a6777746652').removeClass('313933623563376831513d3d');
			$('.3539584b3339586e79746a4b6d614c5233646a573573374d306557556c733359334e6254314e587433646658').hide('200');
		}
		else{
			$('.33647a4f344e7a6777746652').removeClass('313933623563376831513d3d');
			$('.3539584b3339586e79746a4b6d614c5233646a573573374d306557556c733359334e6254314e587433646658').hide('200');
			$(this).addClass('313933623563376831513d3d');
			$(this).children('.324d33633174766330645f4f364f493d').show('200');
		}
	});
	$('.317466623138376c').click(function(){
		$('html, body').animate({
				scrollTop: $('.31637259364e32677a74413d').offset().top
		}, 1000);
	});
	$('.3463335836496d6879745f4b3571553d').click(function(){
		$('html, body').animate({
				scrollTop: $('.31637259364e32677a74413d').offset().top
		}, 1000);
		$('.3463335836413d3d').animate({
				left: "-285px"
		}, 400);
		$('.3463335836413d3d').removeClass("34396a4f34633758");
		$('.3463335836413d3d').addClass("3139546331773d3d");
	});
	$('.3463335836496d6879745f4b3571593d').click(function(){
		$('html, body').animate({
				scrollTop: $('.364e4857324e58637a394353342d6e56792d4c643564445a').offset().top
		}, 1000);
		$('.3463335836413d3d').animate({
				left: "-285px"
		}, 400);
		$('.3463335836413d3d').removeClass("34396a4f34633758");
		$('.3463335836413d3d').addClass("3139546331773d3d");
	});
	$('.3463335836496d6879745f4b3571633d').click(function(){
		$('html, body').animate({
				scrollTop: $('.353950533339586d').offset().top
		}, 1000);
		$('.3463335836413d3d').animate({
				left: "-285px"
		}, 400);
		$('.3463335836413d3d').removeClass("34396a4f34633758");
		$('.3463335836413d3d').addClass("3139546331773d3d");
	});
	$('.3463335836496d6879745f4b3571673d').click(function(){
		$('html, body').animate({
				scrollTop: $('.313966583538725731513d3d').offset().top
		}, 1000);
		$('.3463335836413d3d').animate({
				left: "-285px"
		}, 400);
		$('.3463335836413d3d').removeClass("34396a4f34633758");
		$('.3463335836413d3d').addClass("3139546331773d3d");
	});
	var $animation_elements = $('.353950533339586d675a6e56362d505032396a6335673d3d');
	var $window = $(window);
	$window.on('scroll', check_if_in_view);
	$window.on('scroll resize', check_if_in_view);
	$window.trigger('scroll');

	$('textarea').blur(function () {
    $('#hire textarea').each(function () {
		$this = $(this);
		if ( this.value != '' ) {
			  $this.addClass('3274664d364e7a5978513d3d');
			}
		else {
			  $this.removeClass('3274664d364e7a5978513d3d');
		}
		});
	});

	$('#hire .field:first-child input').blur(function () {
		$('#hire .field:first-child input').each(function () {
			$this = $(this);
			if ( this.value != '' ) {
			  $this.addClass('3274664d364e7a5978513d3d');
			}
			else {
			  $this.removeClass('3274664d364e7a5978513d3d');
			}
		});
	});

	$('#hire .field:nth-child(2) input').blur(function () {
		$('#hire .field:nth-child(2) input').each(function () {
			$this = $(this);
			if ( this.value != '' ) {
			  $this.addClass('3274664d364e7a5978513d3d');
			}
			else {
			  $this.removeClass('3274664d364e7a5978513d3d');
			}
		});
	});
};

function check_if_in_view() {
  var $window = $(window);
  	var cssPercent = 60 ;
	var javaPercent = 35 ;
	var htmlPercent = 75 ;
	var rubyPercent = 15 ;
  var $animation_elements = $('.353950533339586d675a6e56362d505032396a6335673d3d');
  var window_height = $window.height();
  var window_top_position = $window.scrollTop();
  var window_bottom_position = (window_top_position + window_height);

  $.each($animation_elements, function() {
    var $element = $(this);
    var element_height = $element.outerHeight();
    var element_top_position = $element.offset().top;
    var element_bottom_position = (element_top_position + element_height);

    //check to see if this current container is within viewport
    if ((element_bottom_position >= window_top_position) &&
        (element_top_position <= window_bottom_position)) {
      $element.addClass('3364615736644c5932413d3d');
    } else {
      $element.removeClass('3364615736644c5932413d3d');
    }
	if ($element.hasClass('3364615736644c5932413d3d') && $element.hasClass('css')){
		var progressBarWidth1 = cssPercent;
		$element.animate({ width: progressBarWidth1 +"%" }, 750);
		$('<p/>').addClass('33646258324e756730644458334e6e5733513d3d').appendTo($element).text(cssPercent + '%');
	}
	if ($element.hasClass('3364615736644c5932413d3d') && $element.hasClass('html')){
		var progressBarWidth2 = htmlPercent;
		$element.animate({ width: progressBarWidth2 +"%" }, 750);
		$('<p/>').addClass('33646258324e756730644458334e6e5733513d3d').appendTo($element).text(htmlPercent + '%');
	}
	if ($element.hasClass('3364615736644c5932413d3d') && $element.hasClass('javascript')){
		var progressBarWidth3 = javaPercent;
		$element.animate({ width: progressBarWidth3 +"%" }, 750);
		$('<p/>').addClass('33646258324e756730644458334e6e5733513d3d').appendTo($element).text(javaPercent + '%');
	}
	if ($element.hasClass('3364615736644c5932413d3d') && $element.hasClass('ruby')){
		var progressBarWidth4 = rubyPercent;
		$element.animate({ width: progressBarWidth4 +"%" }, 750);
		$('<p/>').addClass('33646258324e756730644458334e6e5733513d3d').appendTo($element).text(rubyPercent + '%');
	}
  });
}

$(document).ready(main);
