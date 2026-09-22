'''Write a program to mine a log file and find out whether it contains ‘python’.'''


with open("logfile.txt", "r") as f:
    content = f.read()
    
if "python" in content:
    print("The word 'python' is present in the log file.")  
else:
    print("The word 'python' is not present in the log file.")