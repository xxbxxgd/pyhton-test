def is_sorted(arr):
    # 判斷數列是否已按照由短到長（從小到大）排序
    return arr == sorted(arr)

def main():
    # 讀取測試資料行數
    t = int(input(""))
    results = []
    for _ in range(t):
        # 讀取一行測試資料（10個數字）
        arr = list(map(int, input("").split()))
        # 判斷是否排序正確，並記錄結果
        if is_sorted(arr):
            results.append("YES")
        else:
            results.append("NO")
    
    # 輸出所有結果
    print("\n".join(results))

if __name__ == "__main__":
    # 主程式入口
    main()
