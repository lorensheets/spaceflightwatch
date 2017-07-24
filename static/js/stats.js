$(document).ready(function() {
  $.getJSON("http://api.open-notify.org/astros.json", function(data) {
    let numPeople = data.number;
    $('#number_of_people').html(numPeople);
  });
});
