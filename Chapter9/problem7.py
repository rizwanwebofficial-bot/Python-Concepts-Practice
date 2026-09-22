with open("logfile.txt", "r") as f:
    lines = f.readlines()


for line in lines:
    if "python" in line:
        print(f"The line number of python in the log file: {lines.index(line) + 1}")
    
