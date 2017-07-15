
/* Launch Table Toggle Expand script */
$(document).ready(function() {
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
