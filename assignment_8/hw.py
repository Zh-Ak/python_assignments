"""
Exercise-1: Count unique elements
"""

def count_unique_elements(my_list: list) -> int:
    n = len(my_list)
    if n == 1:
        return 1
    if n == 0:
        return 0

    count = 1
    my_list.sort()
    for i in range(1, n):
        if my_list[i] != my_list[i - 1]:
            count += 1
    return count

"""
Exercise-2: Remove duplicates
"""

def remove_duplicates(my_list: list) -> list:
    unique_my_list = []
    for i in range(len(my_list)):
        if my_list[i] not in unique_my_list:
            unique_my_list.append(my_list[i])
    return unique_my_list

"""
Exercise-3: Reverse a list
"""

def reverse_list(my_list: list) -> list:
        reversed_my_list = []
        for i in range(len(my_list) - 1, -1, -1):
            reversed_my_list.append(my_list[i])
        return reversed_my_list

"""
Exercise-4: Find the maximum value in a list
"""

def max_value(my_list: list) -> int:
    return max(my_list)

"""
Exercise-5: Find the minimum value in a list
"""

def min_value(my_list: list) -> int:
    return min(my_list)

"""
Exercise-6: Sum all values in a list
Write a function "sum_values(my_list: list) -> int" that takes a 
list of integers and returns the sum of all values in the list.

Example:
sum_values([1, 2, 3, 4, 5]) -> 15
"""

def sum_values(my_list: list) -> int:
    total_sum = 0
    for i in range(len(my_list)):
        total_sum += my_list[i]
    return total_sum

"""
Exercise-7: Find the average of a list
"""

def average(my_list: list) -> float:
    return sum(my_list) / len(my_list)

"""
Exercise-8: Find the index of an element in a list
"""

def find_index(my_list: list, element: int) -> int:
    for i in range(len(my_list)):
        if my_list[i] == element:
            return i
    return -1

"""
Exercise-9: Check if a list is sorted
"""

def is_sorted(my_list: list) -> bool:
    n = len(my_list)
    if n == 0 or n == 1:
        return True
    for i in range(1, len(my_list)):
        if my_list[i - 1] > my_list[i]:
            return False
    return True

"""
Exercise-10: Count the frequency of an element in a list
"""

def count_frequency(my_list: list, element: int) -> int:
    count = 0
    for num in my_list:
        if num == element:
            count += 1
    return count

"""
Exercise-11: Find the mode of a list
"""

def find_mode(my_list: list) -> int:
    frequency ={}
    max_frequency = 0
    mode = None
    n = len(my_list)

    if n == 1:
        return my_list[0]
    #if n == 0:
     #   return None

    for i in range(n):
        if my_list[i] in frequency:
            frequency[my_list[i]] += 1
            if frequency[my_list[i]] > max_frequency:
                max_frequency = frequency[my_list[i]]
                mode = my_list[i]
        else:
            frequency[my_list[i]] = 1
            if frequency[my_list[i]] > max_frequency:
                max_frequency = frequency[my_list[i]]
                mode = my_list[i]

    return mode

"""
Exercise-12: Remove all occurrences of an element in a list
"""

def remove_all(my_list: list, element: int) -> list:
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] != element:
            new_list.append(my_list[i])
    return new_list

"""
Exercise-13: Rotate a list to the left by k positions
"""

def rotate_left(my_list: list, k: int) -> list:
    if not my_list:
        return my_list

    n = len(my_list)
    new_list = [0] * n
    k = k % n

    if k == 0:
        return my_list

    left = k
    for j in range(k):
        new_list[-left] = my_list[j]
        left -= 1

    j = 0
    for i in range(k, len(my_list)):
        new_list[j] = my_list[i]
        j += 1

    return new_list

"""
Exercise-14: Rotate a list to the right by k positions
"""

def rotate_right(my_list: list, k: int) -> list:
    if not my_list:
        return my_list

    n = len(my_list)
    new_list = [0] * n
    k = k % n

    if k == 0:
        return my_list

    j = k
    for i in range(n - k):
        new_list[j] = my_list[i]
        j += 1

    j = 0
    for i in range(n - k, n):
        new_list[j] = my_list[i]
        j += 1

    return new_list

"""
Exercise-15: Find the intersection of two lists (I considered the list to be sorted)
"""

def find_intersection(list1: list, list2: list) -> list:
    if not list1 or not list2:
        return []

    new_list = []
    ptr2 = 0
    for ptr1 in range(len(list1)):
        if list1[ptr1] == list2[ptr2] and list1[ptr1] not in new_list:
            new_list.append(list1[ptr1])
            ptr2 += 1
        elif list1[ptr1] > list2[ptr2]:
            ptr2 += 1

    return new_list

"""
Exercise-16: Find the union of two lists


OR:
sorted(set(list1) | set(list2))
"""

def find_union(list1: list, list2: list) -> list:
    def add_if_new(result, value):
        if not result or value != result[-1]:
            result.append(value)

    new_list = []
    len1 = len(list1)
    len2 = len(list2)
    ptr1 = 0
    ptr2 = 0

    # do until one of the lists is finished
    while ptr1 < len1 and ptr2 < len2:
        if list1[ptr1] < list2[ptr2]:
            add_if_new(new_list, list1[ptr1])
            ptr1 += 1
        elif list1[ptr1] > list2[ptr2]:
            add_if_new(new_list, list2[ptr2])
            ptr2 += 1
        else:
            add_if_new(new_list, list1[ptr1])
            ptr1 += 1
            ptr2 += 1

    # do until second list is finished (in case one is longer)
    while ptr1 < len1:
        add_if_new(new_list, list1[ptr1])
        ptr1 += 1
    while ptr2 < len2:
        add_if_new(new_list, list2[ptr2])
        ptr2 += 1

    return new_list

"""
Exercise-17: Find the difference of two lists
"""

def find_difference(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)
