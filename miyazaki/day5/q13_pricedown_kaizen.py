'''
2024.5.21 宮﨑貴大
価格表を辞書型で定義し、指定した種類の商品の価格を値下げし、値下げ後の価格表を表示するプログラム
入力：値下げ対象の種別、値下げ額
出力：値下げ後の価格表
'''
import sys
args = sys.argv

hm_class = args[1] # 値下げ対象の種別
price_down = int(args[2]) # 値下げ額

# 品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

# 区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")
alcohol = ("ビール", "日本酒")
noodles = ("ラーメン", "うどん", "パスタ")

# 入力された種別から、変更する区分を選定する関数
def class_judgment(select_class):
    if (select_class == "果物類"):
        return fruits
    elif (select_class == "酒類"):
        return alcohol
    elif (select_class == "麺類"):
        return noodles

# 選定された区分を元に、各商品の値下げを行う関数
def price_reduction(kinds):
    for i in kinds:
        discount_amount = hinmoku[i] - price_down
        if (discount_amount < 1):
            discount_amount = 1
        hinmoku[i] = discount_amount


if __name__ == '__main__':

    change_kinds = class_judgment(hm_class)
    price_reduction(change_kinds)

    print(hinmoku, end="")