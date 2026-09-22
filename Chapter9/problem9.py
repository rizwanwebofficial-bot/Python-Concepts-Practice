with open("this.txt", "r") as f:
    content = f.read()
    
    
with open("copy_this.txt", "r") as f:
    copied_content = f.read()
    
if content == copied_content:
    print("The contents of the files are the same.")
    
else:
    print("The contents of the files are different.")