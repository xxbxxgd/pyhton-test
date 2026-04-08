#迴文的定義是從正向,從反向讀取字串都是相同的。
#請寫一個程式判斷總共會讀取 n 個字串,並逐一顯示各個字串是否為迴文;
#是迴文顯示”Yes”,否則顯示”No”。
#輸入:第一行資料為測試資料之筆數,第二行之後為測試資料,
#輸出:對每一組測試資料,輸出判定此測試資料是否為迴文
#輸入範例: 輸出範例: 範例解釋說明
#5          以下共判斷 5 筆輸入
#abcba  Yes  正向、反向讀取字串都相同
#abba   Yes
#bceia  No
#caaci  No
#beaeb  Yes

N = eval(input())
for i in range(N):
    S = input()
    RS = S[::-1]
    if S == RS:
        print('Yes')
    else:
        print('No')