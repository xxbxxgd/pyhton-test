#輸入 1 個字串, 將其字串反轉後且在每個字元間插入豆號輸出, 例如

#輸入:“Orange”, 先反轉成”egnarO”, 在中間插入豆號”e,g,n,a,r,O”.
#注意 1:讀入之字串, 最後面的字元為’\n’(請判斷最後一個字元就不要在迴圈中)
#注意 2:輸出的字串, 最後面不可以有逗號(請判斷最後一個字元就不要再加豆號)
#輸入範例: 輸出範例:
#2
#Orange                  e,g,n,a,r,O
#This is a book.        .,k,o,o,b, ,a, ,s,i, ,s,i,h,T

N = eval(input(''))
for i in range(N):
    S = input()
    RS =S[::-1]
    RV =''
    for rs in RS:
        if RV == '':
            RV = rs
        else:
            RV += f',{rs}'
    print(RV)