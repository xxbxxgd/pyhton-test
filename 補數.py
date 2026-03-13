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