# Write a recursive function called print_between(start, end) which takes two integers as parameters. The function should then print all numbers between (and including) "start" and "end".
def print_between(start, end):
    if start <= end:
        print(start,end=' ')
        print_between(start + 1, end)


print_between(1, 10)