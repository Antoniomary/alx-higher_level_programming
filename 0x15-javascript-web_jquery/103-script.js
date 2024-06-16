$(document).ready(function () {
  function translate () {
    const lang = $('INPUT#language_code').val();
    if (!lang) return;
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#language_code').keypress(function (n) {
    if (n.which === 13) translate();
  });

  $('INPUT#btn_translate').click(function () {
    translate();
  });
});
