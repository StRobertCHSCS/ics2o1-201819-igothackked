word = input("Enter a word:")
new_word = ""

for char in word:
    if char == char:
        new_word = new_word + char + char

print(new_word)