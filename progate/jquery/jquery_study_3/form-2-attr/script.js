$(function() {
  var title = $('#title').text();
  // 2つの変数を定義してください
  var id=$(".section-content p").attr("id");
  var href=$("#link").attr("href");
  $('#title-text').text(title);
  // textメソッドを用いて、それぞれ表示してください
  $("#content-id").text(id);
  $("#link-href").text(href);
});