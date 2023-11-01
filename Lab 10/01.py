def count_down(n):
    if n == 0:
        print("Go!")
        return
    else:
        print(n)
        return count_down(n - 1)

count_down(30)