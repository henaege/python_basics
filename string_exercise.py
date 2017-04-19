# string exercise
example_string = "Who are you?"
example_string_upper = example_string.upper()
print(example_string_upper)

example_string_list = example_string.split(" ")
cap_str = []
for word in example_string_list:
    word = list(word)
    word[0] = word[0].upper()
    word = "".join(word)
    cap_str.append(word)
print (" ".join(cap_str))

reversed_str = []
str_reversed = []
for n in example_string_list:
    n = reversed(list(n))
    n = "".join(n)
    str_reversed.append(n)
for i in range(len(str_reversed)):
    reversed_str.append(str_reversed[-1-i])
print(" ".join(reversed_str))

leetcode = {"A": 4, "E": 3, "G": 6, "I": 1, "O": 0, "S": 5, "T": 7}
example_string = "Leet"
encrypted_str = []
for letter in example_string:
    letter = letter.upper()
    if letter in leetcode.keys():
        encrypted_str.append(str(leetcode[letter]))
    else:
        encrypted_str.append(letter)
print ("".join(encrypted_str))

vowels = ["a", "e", "i", "o", "u"]
example_str = "cheese"
count = 0
for letter in example_str:
    if (letter in vowels):
        count += 1
        if count > 1:
            example_str_list = list(example_str)
            index_of_vowel = example_str_list.index(letter)
            example_str_list.remove(letter)
            example_str_list.insert(index_of_vowel, letter*5)
            after_str = "".join(example_str_list)
print(after_str)

# Caeser
cipher_key = 13
text_message = "lbh zhfg hayrnea jung lbh unir yrnearq"
text_message_list = text_message.split(" ")
de_message = []
for word in text_message_list:
    de_word = ""
    for i in word:
        i = chr((ord(i) - 97 + cipher_key) % 26 + 97)
        de_word += i
    de_message.append(de_word)
print (" ".join(de_message))
