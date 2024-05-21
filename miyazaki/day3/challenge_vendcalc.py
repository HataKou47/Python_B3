# チャレンジ問題（2）
# 自動販売機のおつりを計算する

minimum_amount = 100
merchandise = {"お茶": 110, "コーヒー": 100, "ソーダ": 160, "コーンポタージュ": 130}

sum_amount = 0

def jage_input_amount():
    while True:
        input_amount = int(input("投入金額を入力してください："))
        if (10000 < input_amount):
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
        elif (input_amount < minimum_amount):
            print(f"{input_amount}円では購入できる商品がありません。再度投入金額を入力してください")
        elif ((input_amount%10) != 0):
            print("１円玉、５円玉は使用できません。再度投入金額を入力してください")
        else:
            break

    return input_amount





if __name__ == '__main__':
    print("お茶：110円\n", "コーヒー：100円\n", "ソーダ：160円\n", "コーンポタージュ：130円\n")

    input_amount = jage_input_amount()

    while True:
        input_merchandise = input("何を購入しますか（商品名/cancel）")
        try:
            if (input_merchandise == "cancel"):
                return_change(sum_amount)
            elif (sum_amount == 0):
                return_change(sum_amount)
            elif (sum_amount < minimum_amount):
                return_change(sum_amount)
                sum_amount -= merchandise[input_merchandise]
        except:
            print("そんな商品はありません")

