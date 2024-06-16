$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    if (lang) {
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
