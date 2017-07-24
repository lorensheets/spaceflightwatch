$(document).ready(function() {

  $('.company-icon').on('click', function() {
    var company = $(this).attr('id');
    $('.job-list').removeClass('selected');
    $('#' + company + '__job-list').addClass('selected');

    $('.company-icon').removeClass('active');
    $(this).addClass('active');

    $('.jobs-list__bg').css('background-image', 'url(/static/images/' + company + '.png)');
  });

  $('.capitalize').each(function() {
      let j = $(this).html(); console.log(j);
      j.toLowerCase();
      $(this).html(j);
  });

});
