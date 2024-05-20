# 問15 新幹線の駅間距離を計算しよう２
# 問11「新幹線の駅間を計算しよう」で作成したプログラムに例外処理を追加し、
# 定義済みの駅名以外を入力した場合、「のぞみの停車駅を引数に設定してください」というメッセージを表示する

import sys
args = sys.argv

station1 = args[1]
station2 = args[2]

stations = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

try:
    distanse = round(abs(stations[station1] - stations[station2]), 2)
    print(distanse, end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")