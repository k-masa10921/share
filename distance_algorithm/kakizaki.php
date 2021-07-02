<?php
  /*------------------------- インプット -------------------------*/
  $str_a       = strval(fgets(STDIN));
  $str_b       = strval(fgets(STDIN));
  /*------------------------- 入力文字バリデーション -------------------------*/
  if (preg_match('/[^a-zA-Z0-9]/i', $str_a)) {
    echo 100;
    return ;
  }
  if (preg_match('/[^a-zA-Z0-9]/i', $str_b)) {
    echo 100;
    return ;
  }
  $str_a_len   = strlen($str_a);
  $str_b_len   = strlen($str_b);
  /*------------------------- コスト -------------------------*/
  $delete_cost = 1;
  $insert_cost = 1;
  $change_cost = 1;
  /*------------------------- テーブル初期化 -------------------------*/
  $table[0][0] = 0;
  for ($i=1; $i < $str_a_len; $i++) {
    $table[$i][0] = $i;
  }
  for ($i=1; $i < $str_b_len; $i++) {
    $table[0][$i] = $i;
  }
  /*------------------------- テーブルに値を埋める -------------------------*/
  for ($i=1; $i <= $str_a_len; $i++) {
    for ($j=1; $j <= $str_b_len; $j++) {
      $table[$i][$j] = min([
        $table[$i - 1][$j] + $delete_cost,
        $table[$i][$j - 1] + $insert_cost,
        $table[$i - 1][$j - 1] + ($str_a[$i - 1] === $str_b[$j - 1] ? 0 : $change_cost)
      ]);
    }
  }
  /*------------------------- デバッグ用テーブルを表示 -------------------------*/
  for ($i=0; $i < $str_a_len; $i++) {
    for ($j=0; $j < $str_b_len; $j++) {
      echo $table[$i][$j].' ';
    }
    echo "\n";
  }
  echo $table[$str_a_len - 1][$str_b_len - 1];
?>
