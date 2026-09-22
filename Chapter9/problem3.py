
    
def multiplicationtable(n):
    Table=""
    for i in range(1, 11):
        Table += f"{n} x {i} = {n * i}\n"
    
    with open(f"tables/Table{n}", "w") as f:
        f.write(Table)

for i in range (2, 20):
    multiplicationtable(i)
    
