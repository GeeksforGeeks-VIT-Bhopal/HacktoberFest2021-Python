print("\n\t\t\tProgram to build the Hangman game")
print("\n\t\t\t\t\t\t\t---------WELCOME TO HANGMAN----------\n")
print("Guess the blank spaces to complete the given paragraph")
para="On a spring day,Saba and I went to the park.Once we got to the park, the sky turned Black.It started rain."
print("On a spring day,--- and I went to the park.Once we got to the park, the sky turned ----.It started ----\n")

#list of correct words
words=["Saba","Black","rain"]
lst=[]
guess=""
guess_limit=10
guess_count=0
guesses_over=False
while guess_count<guess_limit:
    guess=input("HINT:Enter the name of person:")
    lst.append(guess)
    guess=input("HINT:Enter the color:")
    lst.append(guess)
    guess=input("HINT:Enter noun:")
    lst.append(guess)
    if lst==words:
        guesses_over=True
        break
    else:
        lst.clear()
        print("\n")
        guess_count +=1

if guesses_over:
    print("Congrats! You have won.")
    print("\nThe complete paragraph is:")
    print("On a spring day,Saba and I went to the park.Once we got to the park, the sky turned Black.It started rain.")
else:
    print("OOPS! Game Over.")