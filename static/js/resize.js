$(document).ready(function() {

  var iOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  var navHeight = (iOS) ? $('nav').height : $('nav').innerHeight;
    $('.top').css('margin-top', navHeight);

  livestream_size = function() {
    let w = window.innerWidth * 0.95;
    let h = w * 0.56;
    let m = "5px auto " + w * 0.05 + "px auto";
    let m2 = w * 0.02 + "px auto 0 auto";
    $('#livestream').css({
      'display': 'block',
      'width': w,
      'height': h,
      'margin': m
    });
    $('.watch-live').css({
      'display': 'block',
      'width': w,
      'margin': m2
    });
    navHeight = $('nav').innerHeight();
    $('.top').css('margin-top', navHeight);
  }

  if (live_stream == true) {

    $(window).on("orientationchange", livestream_size);

    $(window).on("resize", livestream_size);

  } else {

    $(window).on("resize", function() {
      navHeight = $('nav').innerHeight();
      $('.top').css('margin-top', navHeight);
    });

  }



});
