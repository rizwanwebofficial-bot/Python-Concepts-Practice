words = {
    "aam" : "mango",
    "kela" : "banana",
    "saib" : "apple",
    "santra" : "orange",

}

word = input("Enter a word in Hindi: ")
print(words.get(word, "Word not found in dictionary."))