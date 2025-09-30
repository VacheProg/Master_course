def is_possible_to_create_word(letter, word):
    for c in word:
        if c not in letter:
            return False
    return True


x = "napastak"
print("Welcome to Hangman")
print("please insert start the letter to start the game, write 'quit' exit")
letters = []
while not is_possible_to_create_word(letters, x):
    letter = input("please enter letter").strip()
    letters.append(letter)
    for i in x:
        if i in letters:
            print(i, end=' ')
        else:
            print("_", end=' ')


#####
"""
1) fail-i paymany
2) nuyn barna
3) display chi anum tsisth yev sxal tarery
4) haxteluc salyut chi 
5) smaylikov srtik dneq terminlaum vorpes kyanq
6) xaxi skizb yev avart
7) * jamanak

"""




