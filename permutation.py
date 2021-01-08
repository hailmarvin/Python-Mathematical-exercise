## No of of arrangements
permutation = input('Enter Permutation you want e.g(10P2): ')
caps = permutation.upper()
separated = caps.split('P')
n = int(separated[0])
r = int(separated[1])

def factorial(value):
    factorial = 1
    for i in range(1, value+1):
        factorial = factorial * i
    
    return factorial

n_factorial = factorial(n)
dif_factorial = factorial(n-r)

arrangements = n_factorial/dif_factorial
print("There are", int(arrangements), "different arrangements")