$(function() {
  
  // 「#form」要素のsubmitイベントを作成してください
  $("#form").submit(function(){
    var textValue=$("#text-form").val();
    $("#output-text").text(textValue);
    return false;
  });
    
});