def func():
    numbers = []
    Comparisons = 0
    while 1:
        get = int(input(f"Enter a number: "))
        if get == 99999:
            return
        else:
            if not numbers:
                numbers.append(get)
                print(numbers)
            else:
                numbers.append(get)
                for i in range(1, len(numbers) + 1):
                    if numbers[-i] > get:
                        numbers.append(get)
                        print(numbers)

func()