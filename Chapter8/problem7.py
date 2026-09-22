list = ["Harry", "Hermione", "Ron"]

word = input("Enter a word to remove from the list: ")
def remove(word):
    word=word.strip()
    if word in list:
        list.remove(word)
        print(f"{word} has been removed from the list.")
    else:
        print(f"{word} is not in the list.")

remove(word)
print(list)