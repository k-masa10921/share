$(function(){
    var images=['../assets/img_1.jpeg','../assets/img_2.jpeg','../assets/img_3.jpeg','../assets/img_4.jpeg'];
    var count=0;
    $(".change-btn").click(function(){
        if($(this).hasClass("prev")){
            count--;
            $(".check").text(count);
            if(count<0){
                count=images.length-1;
                $("#slide").attr('src',images[count]);
            }else{
                $("#slide").attr('src',images[count]);
            }
        }else if($(this).hasClass("next")){
            count++;
            $(".check").text(count);
            if(count>images.length-1){
                count=0;
                $("#slide").attr('src',images[count]);
            }else{
                $("#slide").attr('src',images[count]);
            }
        }
    });
});