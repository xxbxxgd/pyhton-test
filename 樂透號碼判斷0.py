N =eval(input())

for i in range(N):
    LS =input('').split(' ')
    CLS=[]
    for ls in LS:
        ils =int(ls)
        if (ils>=1 and ils<=49) and (ils not in CLS):
            CLS.append(ils)
        else:
            print('NO')
            break
    
    if len(CLS)==7:
        print('YES')
