#給定一串整數陣列及預期總和,並且透過程式,在輸入的整數陣列中,找出兩
#整數的目錄位置(index)其兩整數滿足相加等於預期總和。假設輸入的整數陣列
#確實只會有一個組合,整數陣列裡的數字不會重複,而且陣列長度不小於 1。
#例如:整數陣列為 2 7 5 11
#預期總和為 9
#因此輸出值為 0 1
#輸入:
#開頭第一行代表測試資料之筆數。接下來每組測試資料各三行。第一行正整數
#為 n,代表此陣列的長度。第二行整數為 m,代表此陣列的預期總合。第三行有
#n 個整數,代表此整數陣列。每個整數之間以半形空白隔開。請參考 Sample
#input。
#輸出:
#對每一組測試資料,輸出整數陣列裡兩整數的目錄(index)位置,此兩整數滿足
#相加等於預期總合。每個整數的目錄位置之間以半形空白隔開。
#輸入範例: 輸出範例:
#2 
#4 
#9
#2 7 5 11   #0 1

#3
#6
#3 2 4      #1 2

N =eval(input())
for i in range(N):
    noL =eval(input())
    Target =eval(input())
    LS =input().split(' ')
    key = False
    RV =''
    for x in range(noL-1):
        for y in range(x+1,noL):
            if eval(LS[x]) + eval(LS[y]) == Target:
                key = True
                RV = f"{x} {y}"
            if key:
                break
        if key:
            break
    print(RV)
        