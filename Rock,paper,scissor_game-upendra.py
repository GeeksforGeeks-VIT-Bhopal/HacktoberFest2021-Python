import random

def gameWin(player1, player2):
    
    if player1 == player2:
        return None

    elif player1 == 'P':
        if player2=='R':
            return False
        elif player2=='S':
            return True
    
    elif player1 == 'R':
        if player2=='S':
            return False
        elif player2=='P':
            return True
    
    elif player1 == 'S':
        if player2=='P':
            return False
        elif player2=='R':
            return True

print("player1 Turn: Paper(P) Rock(R) or Scissor(S)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    player1 = 'P'
elif randNo == 2:
    player1 = 'R'
elif randNo == 3:
    player1 = 'S'

player2 = input("Your Turn: Paper(P) Rock(R) or Scissor(S)?")
a = gameWin(player1,player2)

print(f"Computer chose {player1}")
print(f"You chose {player2}")

if a == None:
    print("The game is a TIE!")
elif a:
    print("You Win!")
else:
    print("You Lose!")