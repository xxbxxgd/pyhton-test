def calculate_future_value(principal, annual_rate, years):
    # 將年利率從百分比轉換為小數
    r = annual_rate / 100
    # 使用公式計算未來價值
    future_value = principal * (1 + r / 12) ** (12 * years)
    return round(future_value)  # 四捨五入至整數

# 讀取測試案例的數量
k = int(input(""))
result = []

# 遍歷每個測試案例
for _ in range(k):
    # 讀取輸入的本金、年利率和計算週期
    principal, annual_rate, years = map(float, input("").split())
    
    # 計算未來價值
    future_value = calculate_future_value(principal, annual_rate, int(years))
    
    # 將結果存入列表
    result.append(future_value)

# 輸出所有結果
for x in result:
    print(x)