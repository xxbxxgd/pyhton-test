def find_median(a, b, c):
    # 找出三個數字中的中間數
    return sorted([a, b, c])[1]

def main():
    # 讀取測試資料組數
    t = int(input(""))
    results = []
    for _ in range(t):
        # 讀取一組測試資料（三個整數）
        a, b, c = map(int, input("").split())
        # 找出中間數並記錄結果
        results.append(find_median(a, b, c))
    
    # 輸出所有結果
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    # 主程式入口
    main()
