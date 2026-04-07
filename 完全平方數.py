#給定兩個正整數 a, b,請找出 a 與 b 之間所有完全平方數的和
#如:兩數 3, 25 中所有完全平方數的和就是 4 + 9 + 16 + 25 = 54
#輸入:第一行資料為測試資料之筆數,第二行之後為測試數值,
#輸出:對每一組測試資料,輸出此測試資料之加總和
#輸入範例: 輸出範例:
#2           
#5 20        25
#3 25        54
import math

N =eval(input())
for i in range(N):
    LS = input().split(' ')
    a =int(LS[0])
    b =int(LS[1])
    x =math.ceil(a**0.5)#a的平方根向上取整
    y =math.floor(b**0.5)#b的平方根向下取整
    sum = 0
    for j in range(x,y+1):
        sum += (j*j)
    print(sum)
