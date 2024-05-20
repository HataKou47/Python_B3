product_value = {'お茶':110, 'コーヒー':100, 'ソーダ':160, 'コーンポタージュ':130}

max_money = 10000
min_money = min(product_value.values())

money = int(input("投入金額を入力してください"))



while True:
    if money > max_money:
        money = input(f"10,000円を超える金額は投入できません。再度投入金額を入力してください")
    elif money < min_money:
        money = input(f"{money}円では購入できる商品がありません。再度投入金額を入力してください")
    elif money % 10 != 0:
        money = input(f"１円玉、５円玉は使用できません。再度投入金額を入力してください")
    else:
        product = input(f"何を購入しますか（商品名/cancel）")
        break

# while product != "cancel":
