$(function() {
  $('.index-btn').click(function() {
    $('.active').removeClass('active');
    var clickedIndex = $('.index-btn').index($(this));
    $('.slide').eq(clickedIndex).addClass('active');
  });
  
  $('.change-btn').click(function() {
    // 変数$displaySlideを定義してください
    var $displaySlide=$(".active");
    
    // 変数$displaySlideからactiveクラスを取り除いてください
    $displaySlide.removeClass("active");
    
    // ifとelseを用いて、$displaySlideの前もしくは次の要素に
    // activeクラスをつけてください
    if($(this).hasClass("next-btn")){
      $displaySlide.next().addClass("active");
    }else{
      $displaySlide.prev().addClass("active");
    }
    
  });
});
