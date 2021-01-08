combination = input('Enter Combinations you want e.g(10C2): ')
caps = combination.upper()
separated = caps.split('C')
n = int(separated[0])
r = int(separated[1])

def factorial(value):
    factorial = 1
    for i in range(1, value+1):
        factorial = factorial * i
    
    return factorial

n_factorial = factorial(n)
r_factorial = factorial(r)
dif_factorial = factorial(n-r)

combinations = n_factorial/(r_factorial*dif_factorial)
print("There are", int(combinations), "different combinations")