# 讀取輸入
k = int(input(""))  # 第一行為測試組數
results = []  # 用來儲存結果

# 處理每一組輸入
for _ in range(k):
    dice = list(map(int, input("").split()))  # 輸入3個點數
    # 判斷是否為豹子
    if dice[0] == dice[1] == dice[2]:
        results.append("Yes")
    else:
        results.append("No")

# 輸出結果
for result in results:
    print(result)