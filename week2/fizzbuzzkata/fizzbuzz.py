for i in range(60):

    if i == 1:
        print("1")
    
    elif i == 2:
        print("2")

    elif i % 3 == 0:
        print("fizz")
        continue

    elif i % 5 == 0:
        print("buzz")
        continue

    elif i % 5 and i % 5 == 0:
        print("fizzbuzz")
        continue

    print(i)