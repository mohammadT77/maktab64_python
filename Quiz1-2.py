s = input("Enter a string: ")

# =============== 2.A ================
vowels = list(filter(lambda c: c.lower() in 'aioeu', s))
print("Vowels list:", vowels)
print("Num of Vowels:", len(vowels))

# =============== 2.B ================
digits = list(filter(str.isnumeric, s))
print("Digits list:", digits)
print("Num of Digits:", len(digits))

# =============== 2.C ================
digits_sum = sum(map(int, digits))
print("Sum of Digits:", digits_sum)


# =============== 2.D ================
# Solution 1:
char_count_dict = {}
for c in s:
    char_count_dict[c] = char_count_dict.get(c, 0) + 1

# Solution 2:
char_count_dict = {c: s.count(c) for c in set(s)}  # Dict comprehension!

print(char_count_dict)
