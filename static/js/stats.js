$(document).ready(function() {
  $.getJSON("http://api.open-notify.org/astros.json", function(data) {
    let numPeople = data.number;
    $('#people_in_space').html(numPeople);
  });

  /*  Handles updating of Voyager Distances from Earth and the Sun  */

  var epoch_0 = 1500825600;
  var epoch_1 = 1500912000;

  var current_time = Math.round(new Date().getTime()/1000); 

  var dist_0_v1 = 20738518374.9197;
  var dist_1_v1 = 20741458818.1222;

  var dist_0_v2 = 17074523862.8607;
  var dist_1_v2 = 17076213313.9471;

  var dist_0_v1s = 20827181160.4370;
  var dist_1_v1s = 20828645026.2431;

  var dist_0_v2s = 17195171118.2343;
  var dist_1_v2s = 17196470067.4883;

  var current_dist_km_v1 = 0;
  var current_dist_au_v1 = 0;

  var current_dist_km_v2 = 0;
  var current_dist_au_v2 = 0;

  var current_dist_km_v1s = 0;
  var current_dist_au_v1s = 0;

  var current_dist_km_v2s = 0;
  var current_dist_au_v2s = 0;

  var au_const = 149597870.691;

  function dist_controller() {

  	current_dist_km_v1 = ( ( ( current_time - epoch_0 ) / ( epoch_1 - epoch_0 ) ) * ( dist_1_v1 - dist_0_v1 ) ) + dist_0_v1;
  	current_dist_au_v1 = (current_dist_km_v1/au_const) + '';
  	current_dist_au_v1 = current_dist_au_v1.split('.');
  	current_dist_au_v1 = current_dist_au_v1[0] + '.' + current_dist_au_v1[1].substring(0,8);

  	current_dist_km_v2 = ( ( ( current_time - epoch_0 ) / ( epoch_1 - epoch_0 ) ) * ( dist_1_v2 - dist_0_v2 ) ) + dist_0_v2;
  	current_dist_au_v2 = (current_dist_km_v2/au_const) + '';
  	current_dist_au_v2 = current_dist_au_v2.split('.');
  	current_dist_au_v2 = current_dist_au_v2[0] + '.' + current_dist_au_v2[1].substring(0,8);

  	current_dist_km_v1s = ( ( ( current_time - epoch_0 ) / ( epoch_1 - epoch_0 ) ) * ( dist_1_v1s - dist_0_v1s ) ) + dist_0_v1s;
  	current_dist_au_v1s = (current_dist_km_v1s/au_const) + '';
  	current_dist_au_v1s = current_dist_au_v1s.split('.');
  	current_dist_au_v1s = current_dist_au_v1s[0] + '.' + current_dist_au_v1s[1].substring(0,8);

  	current_dist_km_v2s = ( ( ( current_time - epoch_0 ) / ( epoch_1 - epoch_0 ) ) * ( dist_1_v2s - dist_0_v2s ) ) + dist_0_v2s;
  	current_dist_au_v2s = (current_dist_km_v2s/au_const) + '';
  	current_dist_au_v2s = current_dist_au_v2s.split('.');
  	current_dist_au_v2s = current_dist_au_v2s[0] + '.' + current_dist_au_v2s[1].substring(0,8);

  	current_dist_lt_v1 = current_dist_km_v1 * 2 / 299792.458;
  	current_dist_lt_v2 = current_dist_km_v2 * 2 / 299792.458;

  	document.getElementById('voyager_1').innerHTML = addCommas( Math.round(current_dist_km_v1) + " KM" );

  	current_time += 1;
  }

  function addCommas(nStr){
  	nStr += '';
  	x = nStr.split('.');

  	x1 = x[0];
  	x2 = x.length > 1 ? '.' + x[1] : '';

  	var rgx = /(\d+)(\d{3})/;

  	while ( rgx.test(x1) ){
  		x1 = x1.replace(rgx, '$1' + ',' + '$2');
  	}
  	return x1 + x2;
  }

  function formatSeconds(num){
  	var hours = Math.floor(num / 3600);
  	num -= (hours * 3600);

  	var minutes = Math.floor(num / 60);
  	num -= (minutes * 60);

  	var seconds = Math.floor(num);

  	if ( hours < 10 )
  		hours = "0" + hours;
  	if ( minutes < 10 )
  		minutes = "0" + minutes;
  	if ( seconds < 10 )
  		seconds = "0" + seconds;

  	return hours + ":" + minutes + ":" + seconds;
  }

  // Start Voyager distance updates
  setInterval(dist_controller,1000);

});
