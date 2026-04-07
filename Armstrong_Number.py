#所謂 Armstrong number 指的是一個 n 位數的整數,它的所有位數的 n 次方
#和恰好等於自己。如:1634 = 1**4 + 6**4 + 3**4 + 4**4
#請依需求(使用者輸入)在一定範圍內找出該範圍內的所有 Armstrong
#numbers.
#輸入說明:
#先輸入代表測資筆數的整數 k(1<=k<=100),每一筆測資包含兩個數字 n, m
#(n<m, n>0, m<=1000000),代表所有尋找 Armstrong number 的範圍。
#輸出說明:
#將所有範圍內的 Armstrong number 依序由小到大輸出,如果沒有找到請輸出
#none。
#輸入範例: 輸出範例:
#2 

#100 999     153 370 371 407
#10 99       none
def IsANO(sX):
    lenX = len(sX)
    CV =0
    for sx in sX:
        CV += int(sx)**lenX

    if CV == int(sX):
        return True
    else:
        return False

N = eval(input())
for i in range(N):
    LS = input().split(' ')
    ST = int(LS[0])
    ED = int(LS[1])
    RLS = []
    for j in range(ST,ED+1):
        if IsANO(str(j)):
            RLS.append(j)
        
    if len(RLS) == 0:
        print('none')
    else:
        for rls in RLS:
            print(f'{rls} ',end='')
        print('')#換行

