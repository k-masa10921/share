$(function() {
  $('#form').submit(function() {
    var selectValue = $('#select-form').val();
    var textValue = $('#text-form').val();
    
    // textValueが空のとき、エラー文を表示してください
    if(textValue == ''){
      $("#error-message").text("理由を記入してください");
    }else{
      $("#error-message").text("");
    }
    
    $('#output-select').text(selectValue);
    $('#output-text').text(textValue);
    return false;
  });
});