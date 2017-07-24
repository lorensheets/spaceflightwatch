window.addEventListener("orientationchange", function() {
  // portrait mode
  if(window.innerHeight > window.innerWidth){
    alert("portrait");
  } else {  // landscape mode
    alert("landscape");
  }
}
