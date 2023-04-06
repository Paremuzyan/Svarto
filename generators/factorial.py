def factorial(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        yield result 
        i += 1
        

for num in factorial(5):
    print(num)
    
