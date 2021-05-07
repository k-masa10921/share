// 1.ボタンの種類でイベント分岐
// 2.activeクラスをsetAttributeで付けることにより画像変更
// 3.最後の画像か最初の画像かで表示画像分岐
// 4.最後の画像か最初の画像かでボタンの表示非表示

//省略変数
const slides = document.getElementById("slides");
const slide = slides.children;
const prev_btn = document.getElementById("prev-btn");
const next_btn = document.getElementById("next-btn");
const index_btn = document.getElementById("index-btn");
const debug = document.getElementById("debug");

//更新変数
const length_slide = slide.length;
var count = 0;
var images = [];
var active = 0;
var index_slide = 0;

//変数の更新
function update_var(){
    images = [...document.querySelectorAll("img")];
    active = document.querySelector("img.fadein");
    index_slide = images.indexOf(active);
}
//ボタンの表示・非表示
function changebtn(){
    prev_btn.classList.add("active");
    next_btn.classList.add("active");
    if(index_slide==0){
        prev_btn.classList.remove("active");
    }else if(index_slide == length_slide-1){
        next_btn.classList.remove("active");
    }
}
//押された番号を取得
function index_clicked(event) {
    var ul = event.target.parentNode;
    var li = ul.querySelectorAll("li");
    clicked_index = Array.prototype.indexOf.call(li, event.target);
    update_var();
    slide[index_slide].classList.remove("fadein");
    slide[clicked_index].classList.add("fadein");
    // debug.innerHTML = clicked_index;
    if(clicked_index==0){
        prev_btn.classList.remove("active");
        next_btn.classList.add("active");
    }else if(clicked_index==length_slide-1){
        next_btn.classList.remove("active");
        prev_btn.classList.add("active");
    }else{
        prev_btn.classList.add("active");
        next_btn.classList.add("active");
    }
}
window.addEventListener("load", function(){
    update_var();
    changebtn();
});
prev_btn.addEventListener("click", function(){
    count --;
    if(0<=count){
        slide[count+1].classList.remove("fadein");
        slide[count].classList.add("fadein");
        debug.innerHTML = count;
    }else{
        debug.innerHTML= "error";
    }
    update_var();
    changebtn();
});
next_btn.addEventListener("click", function(){
    count ++;
    if(count<length_slide){
        slide[count-1].classList.remove("fadein");
        slide[count].classList.add("fadein");
        debug.innerHTML = count;
    }else{
        debug.innerHTML= "error";
    }
    update_var();
    changebtn();
});