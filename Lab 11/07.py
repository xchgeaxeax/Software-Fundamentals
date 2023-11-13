def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)


print(get_gcd(100, 70))

print(get_gcd(2, 6))
