"""
Exercise-1: is_prime
"""

def is_prime(n: int) -> bool:
    if n == 0:
        return False
    if n > 0:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False



"""
Exercise-2: nth_fibonacci
"""

def nth_fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    prev_1 = 0
    prev_2 = 1
    for i in range(3, n + 1):
        current = prev_1 + prev_2
        prev_1, prev_2 = prev_2, current
    return current


"""
Exercise-3: factorial
"""

def factorial(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
Exercise-4: count_vowels
"""

def count_vowels(s: str) -> int:
    count = 0
    for letter in s:
        if letter.lower() in ["a", "e", "o", "u", "i"]:
            count += 1
    return count


"""
Exercise-5: sum_of_digits
"""

def sum_of_digits(n: int) -> int:
    total_sum = 0
    n = abs(n)
    while n > 0:
        remainder = n % 10
        n = n // 10
        total_sum += remainder
    return total_sum


"""
Exercise-6: reverse_string
"""

def reverse_string(s: str) -> str:
    return s[::-1]


"""
Exercise-7: sum_of_squares
"""

def sum_of_squares(n: int) -> int:
    total_sum = 0
    for i in range(n + 1):
        total_sum += i ** 2
    return total_sum


"""
Exercise-8: collatz_sequence_length
"""

def collatz_sequence_length(n: int) -> int:
    if n == 0:
        return 0
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        length += 1
    return length

"""
Exercise-9: is_leap_year
"""

def is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


"""
Exercise-10: count_words
"""

def count_words(s: str) -> int:
    if s == "":
        return 0
    count = 1
    for i in range(len(s) - 1):
        if s[i] == " " and s[i + 1]:
            count += 1
    return count



"""
Exercise-11: is_palindrome
"""

def is_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        return False


"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.
"""

def sum_of_multiples(n: int, x: int, y: int) -> int:
    total_sum = 0
    for i in range(n + 1):
        if i % x == 0 or i % y == 0:
            total_sum += i
    return total_sum

"""
Exercise-13: gcd
"""

def gcd(a: int, b: int) -> int:
    min_value = min(a, b)
    for i in range(min_value, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 0


"""
Exercise-14: lcm
"""

def lcm(a: int, b: int) -> int:
    max_value = a * b
    for i in range(1, max_value + 1):
        if i % a == 0 and i % b == 0:
            return i
    return max_value


"""
Exercise-15: count_characters
"""

def count_characters(s: str, c: str) -> int:
    count = 0
    for letter in s:
        if letter == c:
            count += 1
    return count


"""
Exercise-16: digit_count
"""

def digit_count(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

"""
Exercise-17: is_power_of_two
"""

def is_power_of_two(n: int) -> bool:
    while n > 0 and n % 2 == 0:
        n = n // 2
        print(n)
    if n == 1:
        return True
    else:
        return False


"""
Exercise-18: sum_of_cubes
"""

def sum_of_cubes(n: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 3
    return total_sum

"""
Exercise-19: is_perfect_square
"""

def is_perfect_square(n: int) -> bool:
    if n == 1:
        return True
    for i in range(1, n):
        if i * i == n:
            return True
    return False


"""
Exercise-20: is_armstrong_number
"""

def is_armstrong_number(n: int) -> bool:
    digit_num = digit_count(n)
    initial_num = n
    while n > 0:
        digit = n % 10
        initial_num -= digit ** digit_num
        n = n // 10
    if initial_num == 0:
        return True
    else:
        return False
