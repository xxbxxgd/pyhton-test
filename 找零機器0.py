while True:
    N = eval(input())
    if N == 0:
        break
    
    tN =N
    Ct50 =N//50
    tN = tN -(Ct50*50)
    Ct10 =tN//10
    tN = tN -(Ct10*10)
    Ct5 =tN//5
    tN = tN -(Ct5*5)
    print(f'{Ct50} {Ct10} {Ct5} {tN}')