import random
num = random.randint(1, 9)
player_name = input("Hello mate, What's your name ?\n")
guess_count = 0
print("welcome ", player_name, ", are you ready to plat the guessing game ? (yes/no)"), a = input()
if a == "yes":
    print("I'm guessing a number between 1 to 9")
    while guess_count < 5:
        guess = int(input())
        guess_count += 1
        if guess < num:
            print('Your guess is too low')
        if guess > num:
            print('Your guess is too high')
        if guess == num:
            print("Hurray, you guessed it right!")
            print('You guessed the number in ' + str(guess_count) + ' tries!')
        break
        else:
            print('You did not guess the number, The number was ' + str(num))
else:
    print("hoping to see you soon again! :)")