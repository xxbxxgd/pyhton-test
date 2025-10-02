while True:
    money = int(input(""))

    if money == 0:
        break

    # 定義面額
    denominations = [50, 10, 5, 1]
    result = []

    # 計算各面額鈔票數量
    for denom in denominations:
        count = money // denom
        result.append(count)
        money %= denom

    # 輸出結果
    print(" ".join(map(str, result)))
