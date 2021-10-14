import random

you = input("your turn: Scissor(s) , Rock(r) or Paper(p)?")
print (f"you chose {you}")

print("comp turn :  Scissor(s) , Rock(r) or Paper(p) ?")
randNo = random.randint(1,3)
if   randNo == 1 :
     comp = "s"
elif randNo == 2 :
     comp = "r"
elif randNo == 3 :
     comp = "p"

print (f"computer chose {comp}")

if comp=="s" :
    if you=="s" :
        print ('tie')
    if you=="r" :
        print ('you lose')
    if you=="p" :
        print ('you win')
elif comp=="r" :
    if you=="s" :
        print ('you win')
    if you=="r" :
        print ('tie')
    if you=="p" :
        print ('you loose')
elif comp=="p" :
    if you=="s" :
        print ('you loose')
    if you=="r" :
        print ('you win')
    if you=="p" :
        print ('tie')
