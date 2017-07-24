$(document).ready(function() {
  $.getJSON("http://api.open-notify.org/astros.json", function(data) {
    let numPeople = data.number;
    $('#people_in_space').html(numPeople);
  });
});
