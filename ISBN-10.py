N =eval(input())
for i in range(N):
    S = input()
    sum = 0
    
    for j in range(len(S)):#j=0~8
        sum += int(S[j])*(j+1)

    d = sum&11
    if d == 10:
        print(f'{S}X')
    else:
        print(f'{S}{d}')