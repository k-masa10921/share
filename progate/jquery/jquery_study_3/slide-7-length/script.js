$(function() {
  //change-btnの表示非表示関数
  function toggleChangeBtn() {
    //現在表示されているスライドのインデックス番号を取得
    var slideIndex = $('.slide').index($('.active'));
    //chanage-btnを常時表示
    $('.change-btn').show();
    //スライドインデックス番号によりchange-btnを非表示にする
    if (slideIndex == 0) {
      //0番目ならprev-btnを隠す
      $('.prev-btn').hide();
    } else if (slideIndex == $(".slide").length-1) {
      //一番最後ならnext-btnを隠す
      $('.next-btn').hide();
    }
  }
  //下のスライド番号を押したときのイベント
  $('.index-btn').click(function() {
    //現在のスライドのactiveclass(block)を取り除く
    $('.active').removeClass('active');
    //クリックした番号のインデックス番号を取得
    var clickedIndex = $('.index-btn').index($(this));
    //クリックした番号のスライドにactiveclassを追加
    $('.slide').eq(clickedIndex).addClass('active');
    toggleChangeBtn();
  });
  //change-btnを押したときのイベント
  $('.change-btn').click(function() {
    //現在のactiveスライド
    var $displaySlide = $('.active');
    //現在のスライドのacticeclassを取り除く
    $displaySlide.removeClass('active');
    //押したchange-btnのクラスのより条件分岐
    if ($(this).hasClass('next-btn')) {
      //next-btnを持っていれば、次のスライドにactiveclassを追加
      $displaySlide.next().addClass('active');
    } else {
      //prev-btnを持っていれば、前のスライドにactiveclassを追加
      $displaySlide.prev().addClass('active');
    }
    toggleChangeBtn();
  });
});
