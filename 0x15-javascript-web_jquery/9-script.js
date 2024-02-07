// JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello :
// 1. The translation of hello must be displayed in the HTML tag DIV#hello
// 2. must use the JQuery API
// 3. script must work when it is imported from the <head> tag
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (info) {
    $('#hello').append(info.hello);
});