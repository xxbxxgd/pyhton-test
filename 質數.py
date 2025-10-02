k = int(input(""))
results = []

for _ in range(k):
    n = int(input(""))
    if n < 2:
        results.append(f"{n}: NO")
    elif n in (2, 3):
        results.append(f"{n}: YES")
    elif n % 2 == 0 or n % 3 == 0:
        results.append(f"{n}: NO")
    else:
        i = 5
        is_prime = True
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                is_prime = False
                break
            i += 6
        if is_prime:
            results.append(f"{n}: YES")
        else:
            results.append(f"{n}: NO")

print("\n".join(results))
