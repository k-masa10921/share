$(function(){
  
  // 「.social-icon」にマウスが乗ったときに、そのfont-sizeを30pxに変更し、
  // 離れたときにはfont-sizeを24pxにしてください。
  $(".social-icon").hover(
    function(){
      $(this).animate({
        "font-size":"30px"
      },300);
      
    },
    function(){
      $(this).animate({
        "font-size":"24px"
      },300);
    }
  );
  
  

  
});