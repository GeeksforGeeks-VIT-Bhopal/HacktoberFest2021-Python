import random
player_name1 = input("Hello player 1, What's your name?\n")
player_name2 = input("Hello player 2, What's your name?\n")
guess_count = 0
print("welcome ", player_name1, "and", player_name2, ",this is the number guessing game.")
p1_points = 0
p2_points = 0
while True:
    num = random.randint(1, 9)
    print(player_name1, "type your guess.")
    g1 = int(input())
    print(player_name2, "type your guess.")
    g2 = int(input())
    if g1 == num:
        print("Hurray", player_name1, ",you guessed it right!")
        p1_points += 1
    else:
        print("Sorry", player_name1, ',you guessed it wrong.')
    if g2 == num:
        print("Hurray", player_name2, ",you guessed it right!")
        p2_points += 1
    else:
        print("Sorry", player_name2, ',you guessed it wrong.')
        guess_count += 1
        print("The right number is", num, ".")
    cont = input("Do you both wish to play again? If yes then type 'yes'.\n")

    if cont != 'yes':
        print('Thank you for playing.')
        print(player_name1, ", you had", p1_points, "right out of", guess_count, ".")
        print(player_name2, ", you had", p2_points, "right out of", guess_count, ".")
        if p1_points > p2_points:
            print(player_name1, ", you won the game.")
        elif p1_points < p2_points:
            print(player_name2, ", you won the game.")
        else:
            print("Both have same points, so that's a tie.")
        break