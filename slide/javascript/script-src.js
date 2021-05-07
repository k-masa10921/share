const images = ["../assets/img_1.jpeg","../assets/img_2.jpeg","../assets/img_3.jpeg","../assets/img_4.jpeg"];
const slide = document.getElementById("slide");
var count = 0;
document.getElementById("prev-btn").onclick = function(){
  count--;
  if(count<0){
    count = images.length-1;
    slide.setAttribute('src', images[count]);
  }
  document.getElementById("test").innerHTML = count;
  slide.setAttribute('src', images[count]);
}
document.getElementById("next-btn").onclick = function(){
  count++;
  if(count>images.length-1){
    count = 0;
    slide.setAttribute('src', images[count]);
  }
  document.getElementById("test").innerHTML = count;
  slide.setAttribute('src', images[count]);
}
