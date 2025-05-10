def odd_numbers(a,b):
    return sum(x for x in range(a, b+1) if x % 2 == 1)

a = 4261
b = 8699
result = odd_numbers(a,b)
print(result)