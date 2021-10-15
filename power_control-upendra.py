import os

print("1. Shutdown your Computer after Given Time")
print("2. Restart your Computer after Given Time")
print("3. Exit")

print(end="Enter Choice: ")
choice = int(input())

if choice==1:
    print(end="Enter Number of Seconds: ")
    sec = int(input())
    str1 = "shutdown /s /t "
    str2 = str(sec)
    str = str1+str2
    os.system(str)

elif choice==2:
    print(end="Enter Number of Seconds: ")
    sec = int(input())
    str1 = "shutdown /r /t "
    str2 = str(sec)
    str = str1+str2
    os.system(str)
elif choice==3:
    exit()
else:
    print("Invalid!")







