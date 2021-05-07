// $(".check").show();
$(function(){
    //ボタンが押されたとき
    $(".change-btn").click(function(){
        // 現在の表示スライド、番号、スライドの長さを取得
        var $displaySlide=$(".active");
        var index_displaySlide =$(".slide").index($(".active"));
        var length_Slide=$(".slide").length;
        // ボタンを押したときの表示スライドで分岐
        if(index_displaySlide == length_Slide-1){//最後スライド
            $displaySlide.removeClass("active");
            if($(this).hasClass("next")){
                $(".slide").eq(0).addClass("active");
            } else {    
                $displaySlide.prev().addClass("active");
            }
        }else if(index_displaySlide == 0){//最初スライド
            $displaySlide.removeClass("active");
            if($(this).hasClass("next")){
                $displaySlide.next().addClass("active");
            } else {
                $(".slide").eq(length_Slide-1).addClass("active");
            }
        }else{//それ以外
            $displaySlide.removeClass("active");
            if($(this).hasClass("next")){
                $displaySlide.next().addClass("active");
            } else {
                $displaySlide.prev().addClass("active");
            }
        }
    });
});