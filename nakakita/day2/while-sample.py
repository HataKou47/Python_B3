energy = 3
while energy > 0:
    print("+ 走る")
    print("| energy =", energy)     # +や| はレイアウト
    energy -= 1;                    #この行がなければ無限ループ！
else:
    print("+ 止まる")
    print("| energy =", energy)

# -=は数値にのみ適用できる。変数の値を1減らす
# +=も同様