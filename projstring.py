#Part 1
def name_length(full_name): 
    length = len(full_name) 
    return length 

def last_character(full_name): 
    last_character = full_name[-1] 
    return last_character 

def first_e(full_name): 
    first_e = full_name.find("e") 
    if first_e == -1: 
        first_e = 0 
    return first_e 

def total_words(full_name): 
    name_split = full_name.split() 
    total_words = len(name_split) 
    return total_words 

def first_word(full_name): 
    name_split = full_name.split() 
    first_word = name_split[0] 
    return first_word 

def find_vowels(full_name):
    vowels = set("aeiouAEIOU") 
    total_vowels = 0 
    for char in full_name: 
        if char in vowels: 
            total_vowels += 1 
    return total_vowels 

def capitalize_vowels(full_name): 
    vowels = set("aeiuoAEIOU") 
    capitalized_name = "" 
    for char in full_name: 
        if char in vowels: 
            char = char.upper() 
        capitalized_name += char 
    return capitalized_name 

def symbol_string(full_name): 
    plus_symbol = "+" * 25 
    tilde_symbol = "~" * 35 
    symbol_string = plus_symbol + tilde_symbol + full_name + tilde_symbol + plus_symbol 
    return symbol_string 

def split_name(full_name): 
    middle = len(full_name) // 2 
    half1 = full_name[0:middle] 
    half2 = full_name[middle:] 
    split_name = half1 + ("*" * 70) + half2 
    return split_name 

repeat = True
while repeat:
    full_name = str(input("Please enter your full name: "))
    print() 
    print(f"Your name is {name_length(full_name)} characters long.\n") 
    print(f"The last character is: {last_character(full_name)}\n") 
    print(f"The first 'e' is at position: {first_e(full_name)}\n") 
    print(f"Your name has {total_words(full_name)} words.\n") 
    print(f"Your first name is {first_word(full_name)}.\n") 
    print(f"Your name contains {find_vowels(full_name)} vowels.\n") 
    print(f"Your name with uppercase vowels is: {capitalize_vowels(full_name)}\n") 
    print(f"{symbol_string(full_name)}\n") 
    print(f"{split_name(full_name)}\n")
    r1 = int(input("Do you want to repeat? 1 for yes 0 for quit:\n"))
    if r1 == 0:
        print("Goodbye!")
        repeat = False

#Part 2
poem = """You do not have to be good.
You do not have to walk on your knees
for a hundred miles through the desert repenting.
You only have to let the soft animal of your body
love what it loves.
Tell me about despair, yours, and I will tell you mine.
Meanwhile the world goes on.
Meanwhile the sun and the clear pebbles of the rain
are moving across the landscapes,
over the prairies and the deep trees,
the mountains and the rivers.
Meanwhile the wild geese, high in the clean blue air,
are heading home again.
Whoever you are, no matter how lonely,
the world offers itself to your imagination,
calls to you like the wild geese, harsh and exciting -
over and over announcing your place
in the family of things."""

def mirror(s): #A
    return print(s + s[::-1])
#mirror(poem)
'''repeat = True
while repeat:
    mirror(poem)
    r1 = int(input("Do you want to repeat? 1 for yes 0 for quit:\n"))
    if r1 == 0:
        print("Goodbye!")
        repeat = False'''

def remove(s): #B
    unwant = input("Type letter you want to remove: ")
    if unwant in s:
        return print(s.replace(unwant, ''))
    else:
        return print("Letter not found in poem")
#remove(poem)
'''repeat = True
while repeat:
    remove(poem)
    r1 = int(input("Do you want to repeat? 1 for yes 0 for quit:\n"))
    if r1 == 0:
        print("Goodbye!")
        repeat = False'''

def char_num(s): #C
    alphcount = 0
    ecount = 0
    for char in s:
        if char.isalpha():
            alphcount += 1
            if (char == "e") or (char == "E"):
                ecount += 1
    percente = (ecount / alphcount) * 100
    return print(f"Your text contains {alphcount} alphabetic characters, of which {ecount} ({percente:.2f}%) are 'e'.")
#char_num(poem)
'''repeat = True
while repeat:
    char_num(poem)
    r1 = int(input("Do you want to repeat? 1 for yes 0 for quit:\n"))
    if r1 == 0:
        print("Goodbye!")
        repeat = False'''

def char_num_mod(s): #D
    charcount = 0
    alphcount = 0
    ecount = 0
    for char in s:
        charcount += 1
        if char.isalpha():
            alphcount += 1
            if (char == "e") or (char == "E"):
                ecount += 1
    percente = (ecount / alphcount) * 100
    return print(f"Your text contains {charcount} characters, {alphcount} alphabetic characters, of which {ecount} ({percente:.2f}%) are 'e'.")

def not_e(text): #E
    find_e = text.find("e") 
    if find_e == -1: 
        return True 
    else: 
        return False 

def not_char(text, char): #F
    find_char = text.find(char) 
    if find_char == -1: 
        return True 
    else: 
        return False 

def not_emod(text): #G
    words = text.split()
    no_e = 0
    length = len(words)
    for word in words:
        if not_char(word, 'e'):
            print(word)
            no_e += 1
    percent = (no_e / length) * 100
    return print(f"Perecent of words with no 'e' in the string: {percent:.2f}%")

def avoids(): #H
    word = input("Enter a word: ")
    forbidden = input("Enter a string of forbidden letters: ")
    for letter in forbidden:
        if letter in word:
            print("False")
            return False
    print("True")
    return True

def uses_only(): #I
    letters = input("Input a string of letters: ")
    word = input("Input a word: ")
    for char in word:
        if char not in letters:
            print("False")
            return False
    print("True")
    return True
    
def uses_all(): #J
    word = input("Input a word: ")
    reqletters = input("Input a string of required letters: ")
    for letter in reqletters:
        if letter not in word:
            print("False")
            return False
    print("True")
    return True

def is_abecedarian(): #K
    word = input("Input a word: ")
    for i in range(len(word)-1):
        if word[i] > word[i + 1]:
            print("False")
            return False
    print("True")
    return True

def find(): #L and M
    word = input("Input a word: ")
    char = input("Input a character: ")
    startindex = int(input("Input an index to start at: "))
    for i in range(startindex, len(word)):
        if word[i] == char:
            print(f"Character found at index: {i}")
            return i
    print("-1, character was not found")
    return -1

def is_sorted(s): #N
    words = s.split()
    for i in range(len(words) - 1):
        if words[i] > words[i + 1]:
            print("False, not in ascending order")
            return False
    print("True. words are in ascending order")
    return True

def is_anagram(): #O
    word1 = input("Input the first word: ")
    word2 = input("Input the second word: ")
    for letters in word1:
        if letters not in word2:
            print("False")
            return False
        for letters in word2:
            if letters not in word1:
                print("False")
                return False
    print("True")
    return True

def has_duplicates(): #P
    string = input("Please input a string: ")
    seen = []
    for char in string:
        if char in seen:
            print("True")
            return True
        else:
            seen.append(char)
    print("False")
    return False

def remove_duplicates(): #Q
    string = input("Please input a string: ")
    seen = []
    new = ""
    for char in string:
        if char not in seen:
            seen.append(char)
            new += char
    return print(f"Here is the new string: {new}")
    













        
        












