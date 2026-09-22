list = ["Donkey", "Horse", "Cow", "Sheep", "Goat"]

with open ("file.txt", "r") as f:
    data = f.read()
    
for word in list:
    data = data.replace(word, "####")
    
with open ("file.txt", "w") as f:
    f.write(data)
    