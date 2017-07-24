$(document).ready(function() {
  $.getJSON("http://api.open-notify.org/astros.json", function(data) {
    let numPeople = data.number;
    $('#people_in_space').html(numPeople);
  });

  /*  Handles updating of Voyager Distances from Earth and the Sun  */

  var epoch_0 = 1301500800; //1281510000;
  var epoch_1 = 1301587200; //1281596400;

  var current_time = new Date().getTime()/1000;
  console.log(current_time);
  
  var dist_0_v1 = 17396281625.1305;
  var dist_1_v1 = 17395807835.8111;

  var dist_0_v2 = 14227951893.7668;
  var dist_1_v2 = 14227140609.8932;

  var dist_0_v1s = 17445817009.5116;
  var dist_1_v1s = 17447283910.3447;

  var dist_0_v2s = 14204601577.2787;
  var dist_1_v2s = 14205894342.6130;

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
  	/*document.getElementById('voy1_au').innerHTML = addCommas( current_dist_au_v1 ) + " AU";

  	document.getElementById('voy2_km').innerHTML = addCommas( Math.round(current_dist_km_v2) + " KM" );
  	document.getElementById('voy2_au').innerHTML = addCommas( current_dist_au_v2 ) + " AU";

  	document.getElementById('voy1_kms').innerHTML = addCommas( Math.round(current_dist_km_v1s) + " KM" );
  	document.getElementById('voy1_aus').innerHTML = addCommas( current_dist_au_v1s ) + " AU";

  	document.getElementById('voy2_kms').innerHTML = addCommas( Math.round(current_dist_km_v2s) + " KM");
  	document.getElementById('voy2_aus').innerHTML = addCommas( current_dist_au_v2s ) + " AU";

  	document.getElementById('voy1_lt').innerHTML = formatSeconds(current_dist_lt_v1);
  	document.getElementById('voy2_lt').innerHTML = formatSeconds(current_dist_lt_v2);

  	//alert("dist_controller.addCommas( Math.round(current_dist_km_v1) ): " + addCommas( Math.round(current_dist_km_v1) ));
    */
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
  setInterval(dist_controller(),1000);

});
