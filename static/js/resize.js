$(document).ready(function() {

  $(window).on("orientationchange", function() {
    // portrait mode
    if(window.innerHeight > window.innerWidth){

    } else {  // landscape mode

    }
  });


  $(window).on("resize", function() {

    console.log(live_stream);
    
    if (live_stream == true) {

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
  });

});
