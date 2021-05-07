$(function(){
    var images=['assets/img_1.jpeg','assets/img_2.jpeg','assets/img_3.jpeg','assets/img_4.jpeg'];
    var count=0;
    function slideShow(){
        $("#slide").attr('src',images[count]);
    }
    function check(){
        $(".check").text(count);
    }
    $(".change-btn").click(function(){
        if($(this).hasClass("prev")){
            count--;
            if(count<0){
                count=images.length-1;
                slideShow();
            }else{
                slideShow();
            }
            check();
        }else{
            count++;
            if(count>images.length-1){
                count=0;
                slideShow();
            }else{
                slideShow();
            }
            check();
        }
    });

});