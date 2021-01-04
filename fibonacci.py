value = input('Insert numerical value to calculate: ')
value = int(value)

def calc(value):
    x = 1
    first = 0
    second = 1

    while x < value:
        third = first + second
        first = second
        second = third
        x += 1

    print(third)

calc(value)