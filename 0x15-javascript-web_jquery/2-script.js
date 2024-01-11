$(document).ready(function () {
  // Waiting for the DOM to be fully loaded
  $('#red_header').click(function () {
    // The DIV#red_header is clicked, update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
