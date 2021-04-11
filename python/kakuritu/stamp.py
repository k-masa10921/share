import random
status = 0  # コインの状態
# 0~0.5 裏
# 0.5~1 表
direction = 0  # 進む方向
station = ["東京", "神田", "秋葉原", "御徒街", "上野", "鶯谷", "日暮里", "西日暮里", "田端",
           "駒込", "巣鴨", "大塚", "池袋", "目白", "高田馬場", "新大久保", "新宿", "代々木",
           "原宿", "渋谷", "恵比寿", "目黒", "五反田", "大崎", "品川", "田町", "浜松町", "新橋", "有楽町"]
stamp = ["東京"]  # スタンプ
sum = 0
# 10回試行する
for num in range(10):
    while True:
        status = random.uniform(0, 1)
        if(status > 0.5):  # コインが表なら
            if(direction == len(station)-1):
                direction == 0
            else:
                direction = direction + 1
            stamp.append(station[direction])  # スタンプを追加
        else:  # コインが裏なら
            if(direction == 0):
                direction = len(station)-1
            else:
                direction = direction - 1
            stamp.append(station[direction])
        stamp = list(set(stamp))  # スタンプの重複を削除
        if(len(stamp) == 29):  # スタンプが29個集まれば終了
            break
    if(num == 0):  # 一回目の試行
        answer = station[direction]  # 最後の駅を表示
        print("最後の駅は"+answer)
    else:
        if(answer == station[direction]):
            sum = sum + 1
print(sum/10)
