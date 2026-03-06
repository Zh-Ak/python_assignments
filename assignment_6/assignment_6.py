
# 1
def two_sum(num1, num2):
    return num1 + num2


a = 3
b = 4
print(f"Two_sum of {a}, {b} is {two_sum(a,b)}")


# 2
def reverse_string(word):
    return word[::-1]


word1 = "Hi there!"
print(f"Reverse_string of {word1} is {reverse_string(word1)}")

# 3
def string_length(word):
    count = 0
    for letter in word:
        count += 1
    return count


word2 = "Kolobok"
print(f"Length of the word {word2} is {string_length(word2)}")

# 4
def concatenate_string(str1, str2):
    return str1 + str2


word3 = "Kazakh"
word4 = "stan"
print(f"After concatenation: {concatenate_string(word3, word4)}")

# 5
def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letter in vowels:
        return True
    else:
        return False


letter1 = "A"
letter2 = "b"
print(f"Letter {letter1} is vowel? - {is_vowel(letter1)}")
print(f"Letter {letter2} is vowel? - {is_vowel(letter2)}")

# 6
def swap_first_letter(word):
    new_word = ""
    new_word += word[-1]
    n = len(word) - 1
    for letter in word[1:n]:
        new_word += letter
    new_word += word[-len(word)]
    return new_word


word5 = "Banana" # aananB
print(f"After swapping first and last letter of the word {word5} -> {swap_first_letter(word5)}")

# 7
def to_uppercase(word):
    new_word = ""
    n = ord("A") - ord("a")
    for letter in word:
        if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
            new_word += chr(ord(letter) + n)
        else:
            new_word += letter
    return new_word


word6 = "BanAnANANannaA"
print(f"{word6} -> all uppercase {to_uppercase(word6)}")

# 8
def rectangle_area(length, width):
    return length * width


length = 2
width = 3
print(f"Area of the rectangle with length {length} and width {width} is {rectangle_area(length, width)}")

# 9
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


num1 = 4
print(f"{num1} is even? - {is_even(num1)}")

# 10
def extract_first_three(word):
    count = 0
    for letter in word:
        if count == 3:
            return
        print(letter)
        count += 1


word7 = "Japan"
print(f"Extracted the first three letters of the word {word7}")
extract_first_three(word7)

# 11
age = 23
name = "Zhaniyash"
print(f"String interpolation: My name is {name}, and I am {age} years old.")

# 12
word8 = "Ramadan"
print(word8[2:6])

# 18
num2 = "18"
print(int(num2))

# 14
word9 = "Hi"
print(word9 * 3)

# 15
num3 = 6
num4 = 4
quotient = num3 // num4
remainder = num3 % num4
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# 16
num5 = 5
num6 = 3
print(f"Float division: {num5/num6}")

# 17
word10 = "Banananananaaaa"
print(f"Letter \"a\" occured in the word {word10} {word10.count("a")} times")

# 18
word11 = "I want to print \" double quotes in this text"
print(word11)

# 19
word12 = """
Bananana
Banananananana
Ba ba ba ba ba na na
"""
print(word12)

# 20
base  = 2
exponent = 5
print(f"Base is {base} and exponent is {exponent} -> ВЖУУУХ -> {base ** exponent}")

# 21 Bonus
def is_palindrome(word):
    n = len(word)
    mid = n // 2
    if word[0:mid] == word[n:mid:-1]:
        return True
    else:
        return False


word13 = "racecar"
print(f"Is {word13} palindrome: {is_palindrome(word13)}")


# 22 Bonus
def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for letter in word1:
        if letter in word2:
            continue
        else:
            return False
    return True


word14 = "spar"
word15 = "rasp"
print(f"Are {word14} and {word15} anagram?  {is_anagram(word14, word15)}")