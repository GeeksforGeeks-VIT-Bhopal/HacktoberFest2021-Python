x =int(input("Enter any number :"))
temp_num= x # store a copy of this number
reverse_num=0 # calculate reverse of this number
while(x > 0):
    last_digit = x % 10 # taking out last digit of this number
    reverse_num = reverse_num * 10 + last_digit # appending
    x = x //10 # floor divide the number leaves out the last digit from number
# compare reverse to original number
if(temp_num == reverse_num):
    print("The number", temp_num, "is palindrome!")
else:
    print(temp_num, "is Not a palindrome!")