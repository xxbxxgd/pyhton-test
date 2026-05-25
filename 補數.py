#任意輸入一組二進制值,自動轉成二補數值輸出。(註:2的補數 = 1的補數
#加 1)
#參照以下二組輸入及輸出範例
#輸入:
#第一行資料為測試資料之筆數,第二行之後為測試數值。
#輸出:
#對每一組測試資料,輸出此測試資料之二補數。
#輸入範例: 輸出範例:
#2 
#0110       1010
#01010101   10101011

def BCOne(BS):
    RV =''
    for bs in BS:
        if bs =='0':
            RV += '1'
        if bs =='1':
            RV += '0'
    return RV

N =eval(input())

for i in range(N):
    S =input('')
    BOneS =BCOne(S)
    iBoneS =int(BOneS,2)
    print(f'{iBoneS+1:b}')