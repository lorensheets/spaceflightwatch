$(document).ready(function() {

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
  }

  if (live_stream == true) {

    $(window).on("orientationchange", livestream_size);

    $(window).on("resize", livestream_size);

  }

});
