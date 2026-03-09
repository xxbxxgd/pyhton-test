N = eval(input(''))

for i in range(N):
    LS =input('').split(' ')
    P =eval(LS[0])
    r =eval(LS[1])/100
    t =eval(LS[2])
    F =P*(1+(r/100))**(12+t)
    print(f'{F:.0f}')