<?php
function main($lines) {
  // foreach ($lines as $value) {
		// test zzzz
		// echo $value;
    $split      = explode(' ', $lines[0]);
    if (count($split) != 2){
        echo '1001';
        return ;
    }
    /*------------------------- インプット -------------------------*/
    $str_a       = strval($split[0]);
    $str_b       = strval($split[1]);
    $str_a_len   = strlen($str_a);
    $str_b_len   = strlen($str_b);
    /*------------------------- 入力文字バリデーション -------------------------*/
    for ($i=0; $i < $str_a_len; $i++) {
			// preg_match true=1
      if (preg_match('/^[0-9a-zA-Z]*$/', $str_a[$i]) == 0) {
        echo '1002';
				// 返り値を返すでmainfunction終了
        return ;
      }
    }
    for ($i=0; $i < $str_b_len; $i++) {
      if (preg_match('/^[0-9a-zA-Z]*$/', $str_b[$i]) == 0) {
        echo '1003';
        return ;
      }
    }
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
        if ($str_a[$i - 1] === $str_b[$j - 1]) {
          $cost = $table[$i - 1][$j - 1];
        } else {
          $cost = $table[$i - 1][$j - 1] + $change_cost;
        }
        $table[$i][$j] = min([
          $table[$i - 1][$j] + $delete_cost,
          $table[$i][$j - 1] + $insert_cost,
          $cost,
        ]);
      }
    }
    //文末に改行文字が入っていたため
    //abc空文字で4文字になっていた
    // echo $table[$str_a_len - 1][$str_b_len - 1];
    echo $table[$str_a_len][$str_b_len]."\n";
  // }
}
	$array = array();
	while (true) {
		$stdin = trim(fgets(STDIN));
		// $stdin = fgets(STDIN);
		// 空文字が入ればbreak
		//enterが入力されるとbreak
		if ($stdin == "") {
			break;
		}
		$array[] = $stdin;
	}
	main($array);
?>
