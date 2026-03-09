N =eval(input(''))

for i in range(N):
    LS =input('').split(' ')
    iLS=[]
    for ls in LS:
        iLS.append(eval(ls))
    aLS=iLS[::]
    aLS.sort()
    if iLS == aLS:
        print('Yes')
    else:
        print('No')
