$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      const translation = data.hello;
      $('#hello').text(translation);
    }).fail(function () {
      $('#hello').text('Translation not found');
    });
  });
});
