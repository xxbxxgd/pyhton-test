a =int(input(""))
result =[]

for _ in range(a):
    text =input("")
    text = text.strip()
    reserve = text[::-1]
    x =",".join(text)
    result.append(x)

for n in result:
    print(n)


