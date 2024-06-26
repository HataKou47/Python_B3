# 問11 新幹線の駅間距離を計算しよう
# 辞書型に新幹線駅名と東京駅からの距離を定義し、第2引数と第3引数に設定した駅間の距離を計算し出力（小数第2位まで出力）する

import sys
args = sys.argv

station1 = args[1]
station2 = args[2]

stations = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}


distanse = round(abs(stations[station1] - stations[station2]), 2)

print(distanse, end="")