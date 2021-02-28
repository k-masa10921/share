$(function() {
  $('.index-btn').click(function() {
    $('.active').removeClass('active');
    var clickedIndex = $('.index-btn').index($(this));
    $('.slide').eq(clickedIndex).addClass('active');
    
    // 1. 変数slideIndexに「.active」要素のインデックス番号を代入してください
    var slideIndex = $(".slide").index($(".active"));
    
    // 3. change-btn要素を表示してください
    $(".change-btn").show();
    
    // 2. ifとelse ifを用いて、「.change-btn」の表示/非表示をおこなってください
    if(slideIndex == 0){
      $(".prev-btn").hide();
    }else if(slideIndex == 3){
      $(".next-btn").hide();
    }
    
  });
  
  $('.change-btn').click(function() {
    var $displaySlide = $('.active');
    $displaySlide.removeClass('active');
    if ($(this).hasClass('next-btn')) {
      $displaySlide.next().addClass('active');
    } else {
      $displaySlide.prev().addClass('active');
    }
    
    // 「.index-btn」のクリックイベントと同様の処理を記述してください
    var slideIndex =$(".slide").index($(".active"));
    $(".change-btn").show();
    if(slideIndex == 0){
      $(".prev-btn").hide();
    }else if(slideIndex == 3){
      $(".next-btn").hide();
    }
    
  });
});
