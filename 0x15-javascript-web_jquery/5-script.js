$(document).ready(function () {
  // Waits for DOM to be fully loaded
  $('#add_item').click(function () {
    // When DIV#add_item is clicked, add a new <li> element to UL.my_list
    $('<li>Item</li>').appendTo('.my_list');
  });
});
