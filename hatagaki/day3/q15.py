import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv

f_station = args[1]
t_station = args[2]

distance_dict = {'東京':0.0, '品川':6.78, '新横浜':25.54, 
                     '名古屋':342.02, '京都':476.31, '新大阪':515.35}

try:
    distance = abs(distance_dict[f_station] - distance_dict[t_station])
    print(Decimal(str(distance)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end = "")