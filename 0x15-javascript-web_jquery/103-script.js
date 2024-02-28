$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    fetchTranslation();
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val().trim();
    if (languageCode === '') {
      $('#hello').text('Please enter a language code');
      return;
    }
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      const translation = data.hello;
      $('#hello').text(translation);
    }).fail(function () {
      $('#hello').text('Translation not found');
    });
  }
});
