import sys
station1 =  sys.argv[1]
station2 =  sys.argv[2]


distances = {
    "東京": 0.00,
    "品川":6.78,
    "新横浜":25.54,
    "名古屋":342.02,
    "京都":476.31,
    "新大阪":515.35}
try:
    distance = abs(distances[station1] - distances[station2])
    a = round(distance, 2)
    print(a, end = "")
except:
    print("のぞみの停車駅を引数に設定してください", end = "")