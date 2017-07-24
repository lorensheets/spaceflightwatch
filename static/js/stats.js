$(document).ready(function() {
  $.getJSON("http://api.open-notify.org/astros.json", function(data) {
    let numPeople = data.number;
    $('#people_in_space').html(numPeople);
  });

  $.getJSON("https://www.space-track.org/basicspacedata/query/class/satcat/OBJECT_TYPE/PAYLOAD/orderby/OBJECT_TYPE%20asc/metadata/false", function(data) {
    let numSatellites = 0;
    for (item in data) {
      numSatellites++;
    }
    $('#num_of_satellites').html(numSatellites);
  });
});
