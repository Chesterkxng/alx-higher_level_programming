$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const trans = data.hello;
    $('DIV#hello').text(trans);
  });
});
