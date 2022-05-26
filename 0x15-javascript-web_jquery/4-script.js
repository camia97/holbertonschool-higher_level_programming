#!/usr/bin/node
$('header').addClass('red');
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('green');
});
