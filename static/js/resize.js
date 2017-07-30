$(document).ready(function() {

  function topContentMargin() {
    var navHeight;
    if (window.innerWidth > 768) {
      navHeight = $('nav').innerHeight();
      $('.top').css('margin-top', navHeight);
    } else {
      navHeight = 0;
    }
    $('.top').css('margin-top', navHeight);
  }

  topContentMargin();

  function livestream_size() {
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
  }

  if (live_stream == true) {
    $(window).on("orientationchange", livestream_size);
    $(window).on("orientationchange", topContentMargin);
    $(window).on("resize", livestream_size);
    $(window).on("resize", topContentMargin);
  } else {
    $(window).on("resize", topContentMargin);
    $(window).on("orientationchange", topContentMargin);
  }

});
