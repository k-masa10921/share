<?php namespace Track;
function main($lines) {
  foreach ($lines as $index=>$value) {
    printf("line[%s]: %s\n", $index, $value);
  }
}
$array = array();
while (true) {
  $stdin = fgets(STDIN);
  if ($stdin == "") {
    break;
  }
  $array[] = rtrim($stdin);
}
main($array);
?>
