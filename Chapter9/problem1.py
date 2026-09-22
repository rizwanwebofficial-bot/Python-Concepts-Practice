with open("poem.txt", "w") as f:
    f.write("Twinkle twinkle little star,\n")
    
with open("poem.txt", "r") as f:
    data = f.read()
    print(data)

    if "Twinkle" in data:
        print("The word Twinkle is present in the poem.")
    else:
        print("The word Twinkle is not present in the poem.")
    