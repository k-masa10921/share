// 関数attackの中身を完成させてください
function attack(item) {
  if(item==="手裏剣"){
    return "相手に大ダメージを与えた！";
  }
  return "相手にダメージを与えた！";
}

// 関数attackの引数に「手裏剣」をわたして、関数attackの戻り値をコンソールに出力してください
console.log(attack("手裏剣"));
