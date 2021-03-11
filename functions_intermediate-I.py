# rand_int function solve
import random


def rand_int(min=0, max=100):
    num = round(random.random() * (max-min) + min)
    return num


print(rand_int())
print(rand_int(max=50))
print(rand_int(min=50))
print(rand_int(500, 50))

# edge case check


def rand_int_edge(min=0, max=100):
    if min > max:
        return f"Check input. Min of {min} cannot be greater than Max of {max}."
    else:
        num = round(random.random() * (max-min) + min)
        return num


print(rand_int_edge(10, 4))
