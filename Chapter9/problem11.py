with open("poem.txt", "r") as f:
    content=f.read()
with open("renamed_by_ python.txt", "w") as f:
    f.write(content)