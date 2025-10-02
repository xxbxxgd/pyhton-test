def is_valid_lottery(numbers):
    # 確保所有數字範圍在 1 到 49 且無重複
    return len(numbers) == 7 and all(1 <= num <= 49 for num in numbers) and len(set(numbers)) == 7

def main():
    # 讀取測試資料行數
    n = int(input(""))
    results = []
    for _ in range(n):
        # 讀取一組測試資料（7 個數字）
        numbers = list(map(int, input("").split()))
        # 判斷是否符合樂透號碼規則，並記錄結果
        if is_valid_lottery(numbers):
            results.append("Yes")
        else:
            results.append("No")
    
    # 輸出所有結果
    print("\n".join(results))

if __name__ == "__main__":
    # 主程式入口
    main()
