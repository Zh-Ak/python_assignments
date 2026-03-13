"""
💎 Exercise-1 (Longest Consecutive Sequence):
longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:
    my_set = set(my_list)
    longest = 0
    for num in my_set:
        count = 0
        if num - 1 not in my_set:
            while num in my_set:
                count += 1
                if count > longest:
                    longest = count
                num += 1
    return longest

"""
💎 Exercise-2 (Find missing number):
takes a list of integers from 1 to n. might be unsorted

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    my_set = set(my_list)
    length = len(my_set)

    if length == 1 and my_set == {1}:
        return None

    for num in my_set:
        if num - 1 not in my_set:
            while num in my_set:
                num += 1
            if num == length + 1 + 1:
                return 1
            return num

    return 0

"""
💎 Exercise-3 (Find duplicate number):
takes a list of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    my_set = set(my_list)
    return sum(my_list) - sum(my_set)


"""
💎 Exercise-4 (Group Anagrams):
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""
from collections import defaultdict
def group_anagrams(words: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        result[key].append(word)
    return list(result.values())