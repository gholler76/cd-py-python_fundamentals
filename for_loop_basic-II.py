# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now[-1, "big", "big", -5]
def biggie(arr):
    for num in range(0, len(arr), 1):
        if arr[num] > 0:
            arr[num] = "big"
    return arr


print(biggie([1, -2, 8, -7, -3]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1, 1, 1, 1]) changes the original list to[-1, 1, 1, 3] and returns it
# Example: count_positives([1, 6, -4, -2, -7, -2]) changes the list to[1, 6, -4, -2, -7, 2] and returns it
def count_pos(arr):
    pos_count = 0
    for num in range(0, len(arr), 1):
        if arr[num] > 0:
            pos_count += 1
            print(pos_count)
    arr[len(arr)-1] = pos_count
    return arr


print(count_pos([5, -4, -3, 2, -1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1, 2, 3, 4]) should return 10
# Example: sum_total([6, 3, -2]) should return 7


def sum_total(arr):
    sum = 0
    for num in range(0, len(arr), 1):
        sum += arr[num]
    return sum


print(sum_total([1, 2, 3, 4, 5]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1, 2, 3, 4]) should return 2.5


def average(arr):
    sum = 0
    for num in range(0, len(arr), 1):
        sum += arr[num]
    return sum / len(arr)


print(average([2, 4, 6, 8, 10, 12]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37, 2, 1, -9]) should return 4
# Example: length([]) should return 0


def length(arr):
    return len(arr)


print(length([1, 2, 3, 4, 5]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37, 2, 1, -9]) should return -9
# Example: minimum([]) should return False


def minimum(arr):
    if not arr:
        return "False"
    else:
        min = arr[0]
        for num in range(1, len(arr), 1):
            if arr[num] < min:
                min = arr[num]
        return min


print(minimum([9, 2, 3, 1, 5]))
print(minimum([]))


# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37, 2, 1, -9]) should return 37
# Example: maximum([]) should return False
def maximum(arr):
    if not arr:
        return "False"
    else:
        max = arr[0]
        for num in range(1, len(arr), 1):
            if arr[num] > max:
                max = arr[num]
        return max


print(maximum([9, 2, 3, 11, 5]))
print(maximum([]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37, 2, 1, -9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}
def ultimate_analysis(arr):
    sum = 0
    max = arr[0]
    min = arr[0]
    for num1 in range(1, len(arr), 1):
        if arr[num1] > max:
            max = arr[num1]
        elif arr[num1] < min:
            min = arr[num1]
    for num2 in range(0, len(arr), 1):
        sum += arr[num2]
    dict_values = {'sum_total': sum, 'average': sum / len(arr),
                   'minimum': min, 'maximum': max, 'length': len(arr)}
    return dict_values


print(ultimate_analysis([1, 2, 3, 4, 5]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37, 2, 1, -9]) should return [-9, 1, 2, 37]

def reverse_list(arr):
    for num in range(0, len(arr)//2+1, 1):
        temp = arr[num]
        arr[num] = arr[len(arr)-1-num]
        arr[len(arr)-1-num] = temp
    return arr


print(reverse_list([1, 2, 3, 4, 5]))
