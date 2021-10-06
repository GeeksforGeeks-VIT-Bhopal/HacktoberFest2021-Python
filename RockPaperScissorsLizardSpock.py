print ("**** Let's Play Rock Paper Scissors Lizard Spock ****")
print("Rules:\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nand as it always has, Rock crushes Scissors")
stringPlayer1 = input ("\n\nPlayer 1 Turn: Rock, Paper, Scissors, Lizard, or Spock: ")
stringPlayer2 = input ("Player 2 Turn: Rock, Paper, Scissors, Spock, or Lizard: ")
if (stringPlayer1 == stringPlayer2 ):
    print ("Tie: Both players chose:") + stringPlayer1
        
elif (stringPlayer1 == 'Scissors' and stringPlayer2 == 'Paper'):
    print ("Player 1 wins: Scissors cut Paper.")        

elif (stringPlayer1 == 'Paper' and stringPlayer2 == 'Rock'):
    print ("Player 1 wins: Paper covers Rock.")

elif (stringPlayer1 == 'Rock' and stringPlayer2 == 'Lizard'):
    print ("Player 1 wins: Rock crushes Lizard.")

elif (stringPlayer1 == 'Lizard' and stringPlayer2 == 'Spock'):
    print ("Player 1 wins: Lizard poisons Spock.")
        
elif (stringPlayer1 == 'Spock' and stringPlayer2 == 'Scissors'):
    print ("Player 1 wins: Spock smashes Scissors.")

elif (stringPlayer1 == 'Scissors' and stringPlayer2 == 'Lizard'):
    print ("Player 1 wins: Scissors decapitates Lizard.")

elif (stringPlayer1 == 'Lizard' and stringPlayer2 == 'Paper'):
    print ("Player 1 wins: Lizard eats Paper.")

elif (stringPlayer1 == 'Paper' and stringPlayer2 == 'Spock'):
    print ("Player 1 wins: Paper disproves Spock.")

elif (stringPlayer1 == 'Spock' and stringPlayer2 == 'Rock'):
    print ("Player 1 wins: Spock vaporizes Rock.")

elif (stringPlayer1 == 'Rock' and stringPlayer2 == 'Scissors'):
    print ("Player 1 wins: Rock crushes Scissors.")

                
elif (stringPlayer2 == 'Scissors' and stringPlayer1 == 'Paper'):
    print ("Player 2 wins: Scissors cut Paper.")        

elif (stringPlayer2 == 'Paper' and stringPlayer1 == 'Rock'):
    print ("Player 2 wins: Paper covers Rock.")

elif (stringPlayer2 == 'Rock' and stringPlayer1 == 'Lizard'):
    print ("Player 2 wins: Rock crushes Lizard.")

elif (stringPlayer2 == 'Lizard' and stringPlayer1 == 'Spock'):
    print ("Player 2 wins: Lizard poisons Spock.")
        
elif (stringPlayer2 == 'Spock' and stringPlayer1 == 'Scissors'):
    print ("Player 2 wins: Spock smashes Scissors.")

elif (stringPlayer2 == 'Scissors' and stringPlayer1 == 'Lizard'):
    print ("Player 2 wins: Scissors decapitates Lizard.")

elif (stringPlayer2 == 'Lizard' and stringPlayer1 == 'Paper'):
    print ("Player 2 wins: Lizard eats Paper.")

elif (stringPlayer2 == 'Paper' and stringPlayer1 == 'Spock'):
    print ("Player 2 wins: Paper disproves Spock.")

elif (stringPlayer2 == 'Spock' and stringPlayer1 == 'Rock'):
    print ("Player 2 wins: Spock vaporizes Rock.")

elif (stringPlayer2 == 'Rock' and stringPlayer1 == 'Scissors'):
    print ("Player 2 wins: Rock crushes Scissors.")

        
                
        
else:
            print ("Error: Somebody did not select Rock, Paper, Scissors, Lizard or Spock.")