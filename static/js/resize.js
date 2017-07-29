$(document).ready(function() {

  function topContentMargin() {
    if (window.innerWidth > 768) {
      var navHeight = $('nav').innerHeight(); console.log(navHeight);
    } else {
      var navHeight = 10; console.log(navHeight);
    }
    $('.top').css('margin-top', navHeight);
  }

  topContentMargin();

   $(window).on('resize',topContentMargin);

  livestream_size = function() {
    var w = window.innerWidth * 0.95;
    var h = w * 0.56;
    var m = "5px auto " + w * 0.05 + "px auto";
    var m2 = w * 0.02 + "px auto 0 auto";
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
