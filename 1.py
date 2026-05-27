def NoD(S):
    LS =[]
    for s in S:
        if s not in LS:
            LS.append(s)
    return len(LS)

N= eval(input())
for i in range(N):
    X = input('')
    Key1 =False
    Key2 =False
    
    if NoD(X) == 2:
        Key1=True
    if X[0] != X[1] and X[1] != X[2] and X[2] != X[3]:
        Key2 =True

    if Key1 and Key2:
        print('Yes')
    else:
        print('No')