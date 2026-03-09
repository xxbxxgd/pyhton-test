TLS =input().split(' ')
N =eval(input(''))

for i in range(N):
    LLS =input('').split(' ')
    CT=0
    for lls in LLS:
        if lls in TLS:
            CT+=1
    print(CT)