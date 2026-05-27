#請寫一程式批次將 8 進制表示法的數字,轉為 4 進制表示法。請先輸入欲轉換
#進制的筆數 x,並依序輸入及輸出資料。
#說明:147(8) 轉 10 進制為 103;103(10) 轉 4 進制為 1213(4)

#範例輸入 (8 進制) 範例輸出(4 進制) 範例解釋說明
#4      共 4 筆資料
#7      13
#356    3232
#4      10
#125    1111

N = eval(input())
for i in range(N):
    oS = input()
    oL = len(oS)

    #8 >> 10
    D =0
    dg =0
    for j in range(-1,-1*oL-1,-1):
        D+= (int(oS[j]) * (8**dg))
        dg += 1
    
    nD =D

    #10 >> 4
    xS =''
    while True:
        xS = str(nD % 4) + xS
        if nD > 3:
            nD = nD // 4
        else:
            break

    print(xS)