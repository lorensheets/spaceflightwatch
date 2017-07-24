$(window).on("orientationchange", function() {
  // portrait mode
  if(window.innerHeight > window.innerWidth){
    alert("portrait");
  } else {  // landscape mode
    alert("landscape");
  }
});


$(window).on("resize", function() {
  alert("resize");
});
