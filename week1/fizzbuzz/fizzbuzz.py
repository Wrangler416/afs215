def findAnswer(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2

print(findAnswer(1))
print(findAnswer(2))



def perfectNumber(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

print(perfectNumber(6))


