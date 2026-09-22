p1 = "Make a lot of money" 
p2 = "buy now" 
p3 = "subscribe this"
p4 = "click this"

phrase = input("Enter a phrase: ")

if p1 in phrase or p2 in phrase or p3 in phrase or p4 in phrase:
    print("This is a spam message")
else:
    print("This is not a spam message")