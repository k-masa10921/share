$(function() {
  // 「#hide-btn」要素のclickイベントをつくってください
  $("#hide-btn").click(function(){
    $(".slide").eq(1).fadeOut();
  });
  
});