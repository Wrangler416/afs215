def findAnswer(i):
        if i == 1:
            return 1 
         
        if i == 2:
            return 2
        
        if i % 5 == 0 and i % 3 == 0:
            return "fizzbuzz"

        if i % 3 == 0:
            return "fizz"
        
        if i % 5 == 0:
            return "buzz"

        
print(findAnswer(1))
print(findAnswer(2))
print(findAnswer(3))
print(findAnswer(5))
print(findAnswer(6))
print(findAnswer(10))
print(findAnswer(15))

