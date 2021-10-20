sub1 = int(input("Enter your marks in Subject_1 - "))
sub2 = int(input("Enter your marks in Subject_2 - "))
sub3 = int(input("Enter your marks in Subject_3 - "))

subTotal = sub1 + sub2 + sub3

if subTotal < 120  :
    print("You Failed because your aggregate is less than 40%")
elif sub1 or sub2 or sub3 <33:
    print("You Failed because your subject wise score is less than 33%")
else :
    print("Congratulations!! You Passed the exam")