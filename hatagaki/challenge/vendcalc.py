def output_product(product_value):
    for k,v in product_value.items():
        print(f"{k}：{v}円")

def receive_money():
    money = int(input("投入金額を入力してください："))

    while True:
        if money % 10 != 0:
            money = int(input(f"１円玉、５円玉は使用できません。再度投入金額を入力してください："))
        elif money > max_money:
            money = int(input(f"10,000円を超える金額は投入できません。再度投入金額を入力してください："))
        elif money < min_money:
            money = int(input(f"{money}円では購入できる商品がありません。再度投入金額を入力してください："))
        else:
            break

    return money 


def receive_product():

    while True:
        product = input(f"何を購入しますか（商品名/cancel）：")
        if is_exist(product, product_value):
            return product    
        elif product == "cancel":
            money_dict = calc_oturi(money)
            print(f"おつり")
            for k,v in money_dict.items():
                print(f"{k}円玉：{v}枚") 
            exit()
        print(f"その商品は存在しません。もう一度入力してください")


def is_exist(key, product_value):

    if key in product_value:
        return True
    
    return False


def is_check(money, product, product_value):
    if money >= product_value[product]:
        return True
    
    return False


def calc_candidates(money, product_value):
    cands_dict = dict()

    for k,v in product_value.items():
        if money >= v:
            cands_dict[k] = v

    return cands_dict


def update_display_money(money, product, product_value):
    money -= product_value[product]
    print(f"残金：{money}円") 

    return money


def can_continue(money, min_money):

    if money == 0:
        return False
    elif money < min_money:
        money_dict = calc_oturi(money)
        print(f"おつり")
        for k,v in money_dict.items():
            print(f"{k}円玉：{v}枚") 
        return False
    
    return True


def judge_continue(money):
    yisi = input(f"続けて購入しますか(Y/N)")
    if yisi == "Y":
        return True
    else:
        money_dict = calc_oturi(money)
        print(f"おつり")
        for k,v in money_dict.items():
            print(f"{k}円玉：{v}枚") 
        return False


def calc_oturi(money):
    money_type = [10000, 5000, 2000, 1000, 500, 100, 50, 10]
    money_dict = dict()

    for i in money_type:
        if money >= i:
            money_dict[i] = money // i
            money -= money_dict[i] * i

    return money_dict


product_value = {'お茶':110, 'コーヒー':100, 'ソーダ':160, 'コーンポタージュ':130}

max_money = 10000
min_money = min(product_value.values())

output_product(product_value)
money = receive_money()

while True:
    product = receive_product()
    candidates_dict = calc_candidates(money, product_value)

    while is_check(money, product, product_value) == False:
        print(f"あなたの残金ではその商品は買えません。")
        print(f"あなたが変える商品は以下になります。")
        output_product(candidates_dict)
        product = receive_product()   

    money = update_display_money(money, product, product_value)

    if can_continue(money, min_money):
        if judge_continue(money):
            output_product(product_value)
        else:
            break
    else:
        break