$(function() {
  $('#second-btn').click(function() {
    // 「.active」要素からactiveクラスを取り除いてください
    $(".active").removeClass("active");
    
    // 2つ目の「.slide」要素にactiveクラスをつけてください
    $(".slide").eq(1).addClass("active");
    
  });
});
