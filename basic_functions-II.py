# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    arr_count = []
    for val in range(num, -1, -1):
        arr_count.append(val)
    return arr_count


print(countdown(7))


# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(arr):

    print(arr[0])
    return(arr[1])


print(print_and_return([2, 4]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


def add_len(arr):
    add_first_and_length = arr[0] + len(arr)
    return add_first_and_length


print(add_len([2, 4, 6, 8, 10, 12]))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return FalseExample: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]Example: values_greater_than_second([3]) should return False


def values_greater_than_second(arr):
    new_list = []
    for num in range(0, len(arr), 1):
        if len(arr) < 2:
            return "False Example"
        elif arr[num] > arr[1]:
            new_list.append(arr[num])
    print(len(new_list))
    return new_list


print(values_greater_than_second([5, 8, 11, 2, 3, 88, 1, 4]))
print(values_greater_than_second([6]))


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.Example: length_and_value(4,7) should return [7,7,7,7]Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def length_and_value(arr):
    result = []
    for num in range(0, arr[0], 1):
        result.append(arr[1])
    return result


print(length_and_value([7, 15]))
