#!/usr/bin/node

$(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.getJSON(
    `https://fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
    function (data) {
      $('#hello').text(data.hello);
    }
    );
  });
});
