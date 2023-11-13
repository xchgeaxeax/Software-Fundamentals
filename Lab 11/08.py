def collatz(n):
    print(n)
    if n == 1:
        return None
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz((3 * n) + 1)




collatz(12)