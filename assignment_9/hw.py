"""
Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.

Example:
missing_elements([1, 2, 4, 6, 7]) -> [3, 5]
"""

def missing_elements(my_list: list) -> list:
    missing = []

    for i in range(len(my_list) - 1):
        current = my_list[i]
        next_val = my_list[i + 1]

        for num in range(current + 1, next_val):
            missing.append(num)

    return missing

"""
Exercise-2: Count occurrences (return dict)
"""

def count_occurrences(my_list: list) -> dict:
    d = {}
    for i in my_list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


"""
Exercise-4: Common elements
Write a function "common_elements(list1: list, list2: list) -> list" that takes two
lists of integers and returns a list of unique common elements.

Example:
common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def common_elements(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))

"""
Exercise-5: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.

Example:
char_frequency('hello world') -> {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""

def char_frequency(my_string: str) -> dict:
    d = {}
    for c in my_string:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

"""
Exercise-6: Unique words
Write a function "unique_words(my_string: str) -> int" that takes a
string and returns the number of unique words in the string.

Example:
unique_words('hello world hello') -> 2
"""

def unique_words(my_string: str) -> int:
    return len(set(my_string.split()))
"""
Exercise-7: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.

Example:
word_frequency('hello world hello') -> {'hello': 2, 'world': 1}
"""

def word_frequency(my_string: str) -> dict:
    word_list = my_string.split()
    d = {}
    for word in word_list:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

"""
Exercise-8: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.

Example:
count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4) -> 3
"""

def count_in_range(my_list: list, start: int, end: int) -> int:
    unique = set()

    for num in my_list:
        if start <= num <= end:
            unique.add(num)

    return len(unique)
"""
Exercise-9: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
if you face duplicates, the first key should be saved.

Example:
swap_dict({1: 'a', 2: 'b', 3: 'c'}) -> {'a': 1, 'b': 2, 'c': 3}
"""

def swap_dict(d: dict) -> dict:
    d_new = {}
    for key, value in d.items():
        if value not in d_new:
            d_new[value] = key
    return d_new


"""
Exercise-10: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.

Example:
is_subset({1, 2, 3, 4, 5}, {3, 4, 5}) -> True
"""

def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)

"""
Exercise-11: Intersection of lists
Write a function "list_intersection(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in both lists.

Example:
list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1).intersection(set(list2)))

"""
Exercise-12: Union of lists
Write a function "list_union(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in either of the lists.

Example:
list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [1, 2, 3, 4, 5, 6, 7]
"""

def list_union(list1: list, list2: list) -> list:
    return list(set(list1).union(set(list2)))

"""
Exercise-13: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.

Example:
most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 1
"""

def most_frequent(my_list: list) -> int:
    frequency ={}
    max_frequency = 0
    mode = None
    n = len(my_list)

    if n == 1:
        return my_list[0]

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
Exercise-14: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.

Example:
least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 3
"""

def least_frequent(my_list: list) -> int:
    frequency = {}

    for num in my_list: # collect data
        frequency[num] = frequency.get(num, 0) + 1

    l_frequency = float('inf')
    l_frequent = None

    for num, freq in frequency.items(): # analyze
        if freq < l_frequency:
            l_frequency = freq
            l_frequent = num

    return l_frequent


