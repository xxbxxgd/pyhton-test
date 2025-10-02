def is_palindrome(s):
    # 判斷字串是否為迴文
    return s == s[::-1]

def main():
    # 讀取測試案例的數量
    n = int(input(""))
    results = []
    for _ in range(n):
        # 讀取一個測試字串
        test_string = input("")
        # 判斷字串是否為迴文，並記錄結果
        if is_palindrome(test_string):
            results.append(f"{test_string}: Yes")
        else:
            results.append(f"{test_string}: No")
    
    # 輸出所有結果
    print("\n".join(results))

if __name__ == "__main__":
    # 主程式入口
    main()
