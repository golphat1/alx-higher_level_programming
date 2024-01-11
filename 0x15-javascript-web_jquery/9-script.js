$(document).ready(function () {
  // Waits the DOM to be fully loaded
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Fetches the data from the provided URL
    const helloTranslation = data.hello;

    // Updates the text of the <div> with the ID "hello"
    $('#hello').text(helloTranslation);
  });
});
