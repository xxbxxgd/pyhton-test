def calculate_539_matches():
    # 讀取開獎號碼
    winning_numbers = list(map(int, input().split()))

    # 讀取測試組數
    k = int(input())

    results = []

    for _ in range(k):
        # 讀取每組測試的對獎號碼
        ticket_numbers = list(map(int, input().split()))

        # 計算對中的號碼個數
        match_count = len(set(winning_numbers) & set(ticket_numbers))

        # 將對中個數加入結果列表
        results.append(str(match_count))

    # 按行輸出所有結果
    print("\n".join(results))

# 範例使用方法：
# 呼叫函數執行計算
if __name__ == "__main__":
    calculate_539_matches()
