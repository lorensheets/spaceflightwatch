$(document).ready(function() {

  $('.company-icon').on('click', function() {
    var company = $(this).attr('id');
    $('.job-list').removeClass('selected');
    $('#' + company + '__job-list').addClass('selected');

    $('.company-icon').removeClass('active');
    $(this).addClass('active');

    $('.jobs-list__bg').css('background-image', 'url(/static/images/' + company + '.png)');
  });

  function capitalize_Words(str) {
    return str.replace(/\w\S*/g, function(txt){
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
  }
  $('.capitalize').each(function() {
      let j = $(this).html();
      j.toString().toLowerCase(); console.log(j);
      capitalize_Words(j);
      $(this).html(j);
  });

});
