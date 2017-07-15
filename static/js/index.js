$(document).ready(function() {

  var y = new Date().getFullYear();
  date = date + " " + y;
  function formatDate(date) {
    let d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    return [year, month, day].join('-');
  }
  date = formatDate(date);

  var time_utc;

  // get just the GMT time or TBD
  if (time != "TBD") {
    let gmt = time.indexOf("GMT");
    let dash = time.indexOf("-");
    time = time.slice(0,gmt);
    time = time.slice(0,dash);
    time = time.substr(0,2) + ":" + time.substr(2);
    if(time.length < 5){
      time = time + ":00";
    }
    time_utc = moment.utc(date + " " + time);
  }
  var offset = new Date().getTimezoneOffset();
  time_local = time_utc - offset;
  time_local_utc = moment.utc(time_utc - offset);
  time_formatted = moment(time_local).format('MMMM Do YYYY, h:mm:ss a');
  time_diff = time_local_utc - moment.utc();

  setInterval(function() {
    let now = moment.utc();
    let dt = time_local_utc - now;
    let sign = dt < 0 ? "+" : "-";
    let delta = Math.abs(dt) / 1000;
    let countdown = "";

    // calculate (and subtract) whole days
    let days = Math.floor(delta / 86400);
    delta -= days * 86400;

    // calculate (and subtract) whole hours
    let hours = Math.floor(delta / 3600) % 24;
    delta -= hours * 3600;

    // calculate (and subtract) whole minutes
    let minutes = Math.floor(delta / 60) % 60;
    delta -= minutes * 60;

    // what's left is seconds
    let seconds = Math.floor(delta % 60);

    switch(days) {
      case 2:
        countdown += days + " days ";
        break;
      case 1:
        countdown += days + " day ";
        break;
      case 0:
        coundown = "";
        break;
    }
    if (hours > 0) {
      if (hours > 1) {
        countdown += hours + " hours ";
      } else {
        countdown += hours + " hour ";
      }
    } else {
      if (days > 0) {
        countdown += hours + " hours ";
      }
    }
    if (minutes > 0) {
      if (minutes > 1) {
        countdown += minutes + " minutes ";
      } else {
        countdown += minutes + " minute ";
      }
    } else {
      if (hours > 0) {
        countdown += minutes + " minutes ";
      }
    }
    if (seconds == 1) {
      countdown += seconds + " second ";
    } else {
      countdown += seconds + " seconds ";
    }

    $('.t-minus').html("T" + sign + " " + countdown);

  }, 1000);

  $('.launch-date').html("LAUNCHING ON: " + time_formatted);


  // Watch Live script

  if ( (time_diff/1000 < 172800) && (time_diff/1000 > -3600)) {
    var w = window.innerWidth * 0.7;
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


  // Launch Table Toggle Expand script

  $('.expand').click(function() {

    var thisTxt = $(this).text() == 'View More' ? 'View Less' : 'View More';
    var launchContainerHeight = $('.launch-table').css('height') == '200px' ? window.innerHeight * 0.7 + 'px' : '200px';
    var launchTableHeight = $('.launch-table-container').css('height') == '190px' ? ( window.innerHeight * 0.7 ) - 10 + 'px' : '190px';
    var scroll = $('#launchTable').offset().top - 140;
    var overflow = $('.launch-table-container').css('overflow') == 'scroll' ? 'hidden' : 'scroll';

    $('.launch-table-container').css('overflow',overflow);

    $('.launch-table').animate({
      'height': launchContainerHeight
    }, 500, 'easeInOutQuad');

    $('.launch-table-container').animate({
      'height': launchTableHeight
    }, 500, 'easeInOutQuad');

    $('html, body').animate({scrollTop: scroll},500,'easeInOutQuad');

    $(this).text(thisTxt);

  });
  
});
