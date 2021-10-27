import time

import random

# welcome script

time.sleep(1.5)

print('-----------------------------------Welcome to Tic-Tac-Toe-----------------------------------')

time.sleep(0.5)

print('This game is made by Devesh\n')

# variable's

win = 0

lose = 0

X = 'X'

O = 'O'

# definitions

def win_check():

    global r1, r2, r3, r4, r5, r6, r7, r8, r9

    global X_win, O_win, tie

    global u_name, u2_name

    global win

    if r1 == 'X' and r2 == 'X' and r3 == 'X':

        X_win = True

    elif r4 == 'X' and r5 == 'X' and r6 == 'X':

        X_win = True

    elif r7 == 'X' and r8 == 'X' and r9 == 'X':

        X_win = True

    elif r1 == 'X' and r4 == 'X' and r7 == 'X':

        X_win = True

    elif r2 == 'X' and r5 == 'X' and r8 == 'X':

        X_win = True

    elif r3 == 'X' and r6 == 'X' and r9 == 'X':

        X_win = True

    elif r1 == 'X' and r5 == 'X' and r9 == 'X':

        X_win = True

    elif r3 == 'X' and r5 == 'X' and r7 == 'X':

        X_win = True

    elif r1 == 'O' and r2 == 'O' and r3 == 'O':

        O_win = True

    elif r4 == 'O' and r5 == 'O' and r6 == 'O':

        O_win = True

    elif r7 == 'O' and r8 == 'O' and r9 == 'O':

        O_win = True

    elif r1 == 'O' and r4 == 'O' and r7 == 'O':

        O_win = True

    elif r2 == 'O' and r5 == 'O' and r8 == 'O':

        O_win = True

    elif r3 == 'O' and r6 == 'O' and r9 == 'O':

        O_win = True

    elif r1 == 'O' and r5 == 'O' and r9 == 'O':

        O_win = True

    elif r3 == 'O' and r5 == 'O' and r7 == 'O':

        O_win = True

    if O_win:

        win = True

        return print('Winner is', u2_name.upper()), win

    if X_win:

        win = True

        return print('Winner is', u_name.upper(), '\n--Game Ends--\n'), win

    if r1 != '-' and r2 != '-' and r3 != '-' and r4 != '-' and r5 != '-' and r6 != '-' and r7 != '-' and r8 != '-' and r9 != '-':

        tie = True

        return print('This game is a tie'), tie

def rule():

    print('It seems you have some Trouble while play game, now worry i will help you.')

    print('In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X')

    print('For example:')

    print(" X | O | X \n ---------- \n X | X | O \n ----------\n X | O | O \n")

def check_game_o():

    global r1, r2, r3, r4, r5, r6, r7, r8, r9, command_2

    retry_check = False

    if command_2 == 1 and r1 == '-':

        r1 = O

    elif command_2 == 2 and r2 == '-':

        r2 = O

    elif command_2 == 3 and r3 == '-':

        r3 = O

    elif command_2 == 4 and r4 == '-':

        r4 = O

    elif command_2 == 5 and r5 == '-':

        r5 = O

    elif command_2 == 6 and r6 == '-':

        r6 = O

    elif command_2 == 7 and r7 == '-':

        r7 = O

    elif command_2 == 8 and r8 == '-':

        r8 = O

    elif command_2 == 9 and r9 == '-':

        r9 = O

    elif command_2 == 1 and r1 != '-' or command_2 == 2 and r2 != '-' or command_2 == 3 and r3 != '-' or command_2 == 4 and r4 != '-' or command_2 == 5 and r5 != '-' or command_2 == 6 and r6 != '-' or command_2 == 8 and r8 != '-' or command_2 == 7 and r7 != '-' or command_2 == 9 and r9 != '-':

        while not retry_check:

            command_2 = int(input("Don't be Over smart! Try a place which is available as you can not over write a "

                                  "place: "))

            check_game_o()

            retry_check = True

    elif command_2 > 9:

        retry_check = False

        while not retry_check:

            command_2 = int(input("Please select a number between 1-9 ONLY: "))

            check_game_o()

            retry_check = True

    return r1, r2, r3, r4, r5, r6, r7, r8, r9

def check_game_x():

    global r1, r2, r3, r4, r5, r6, r7, r8, r9, command

    retry_check = False

    if command == 1 and r1 == '-':

        r1 = X

    elif command == 2 and r2 == '-':

        r2 = X

    elif command == 3 and r3 == '-':

        r3 = X

    elif command == 4 and r4 == '-':

        r4 = X

    elif command == 5 and r5 == '-':

        r5 = X

    elif command == 6 and r6 == '-':

        r6 = X

    elif command == 7 and r7 == '-':

        r7 = X

    elif command == 8 and r8 == '-':

        r8 = X

    elif command == 9 and r9 == '-':

        r9 = X

    elif command == 1 and r1 != '-' or command == 2 and r2 != '-' or command == 3 and r3 != '-' or command == 4 and r4 != '-' or command == 5 and r5 != '-' or command == 6 and r6 != '-' or command == 8 and r8 != '-' or command == 7 and r7 != '-' or command == 9 and r9 != '-':

        while not retry_check:

            command = int(input("Don't be Over smart! Try a place which is available as you can not over write a "

                                "place: "))

            check_game_x()

            retry_check = True

    elif command > 9:

        retry_check = False

        while not retry_check:

            command = int(input("Please select a number between 1-9 ONLY: "))

            check_game_x()

            retry_check = True

    return r1, r2, r3, r4, r5, r6, r7, r8, r9

def computer_turn():

    global r1, r2, r3, r4, r5, r6, r7, r8, r9, command_2

    global comp_turn

    comp_turn = False

    while not comp_turn:

        command_2 = random.randrange(1, 10)

        if command_2 == 1 and r1 == '-':

            r1 = O

            comp_turn = True

        elif command_2 == 2 and r2 == '-':

            r2 = O

            comp_turn = True

        elif command_2 == 3 and r3 == '-':

            r3 = O

            comp_turn = True

        elif command_2 == 4 and r4 == '-':

            r4 = O

            comp_turn = True

        elif command_2 == 5 and r5 == '-':

            r5 = O

            comp_turn = True

        elif command_2 == 6 and r6 == '-':

            r6 = O

            comp_turn = True

        elif command_2 == 7 and r7 == '-':

            r7 = O

            comp_turn = True

        elif command_2 == 8 and r8 == '-':

            r8 = O

            comp_turn = True

        elif command_2 == 9 and r9 == '-':

            r9 = O

            comp_turn = True

    return r1, r2, r3, r4, r5, r6, r7, r8, r9, print('I choose', command_2)

def write_log():

    global u_name, u2_name, X_win, O_win

    global r1, r2, r3, r4, r5, r6, r7, r8, r9

    log = open('log.txt', 'a')

    log.seek(0)

    if X_win:

        vb = u_name

    elif O_win:

        vb = u2_name

    else:

        vb = 'Tie'

    log.write('\n {} vs {} | {}'.format(u_name, u2_name, vb).upper())

    log.seek(0)

    log.write("\n\n {} | {} | {} \n ---------- \n {} | {} | {} \n ----------\n {} | {} | {}\n\n\n".format(r1, r2, r3, r4, r5, r6, r7, r8, r9))

def read_log():

    log = open('log.txt', 'r')

    log.seek(0)

    print('\n\n')

    print(log.read(),'\n\n')

rule()

time.sleep(0.5)

print('Type * -h or help * to see how to play this Game...')

time.sleep(0.5)

while True:

    r1 = '-'

    r2 = '-'

    r3 = '-'

    r4 = '-'

    r5 = '-'

    r6 = '-'

    r7 = '-'

    r8 = '-'

    r9 = '-'

    u_name = 'Player 1'

    u2_name = 'Player 2'

    X_win = False

    O_win = False

    comp_turn = False

    win = False

    tie = False

    input_1 = input('>Tic-Tac-Toe> ').lower()

    if input_1 == '-h' or input_1 == 'help' or input_1 == 'options':

        print('Welcome to Help box:)')

        print('Here are all options and everything you can do with this Game.\n')

        print('-----------------------------------------------------------------------')

        print('| Options                 | Use                                       |')

        print('-----------------------------------------------------------------------')

        print('| -h or help              | To see all available options for the game.|')

        print('''| About                   | To see information about the developer of |

|                         | this Game                                 |''')

        print('| Start game or New game  | To start a new game.                      |')

        print('| Log/stats/db_load       | To see previous stats of the game.                |')

        print('| Rule                    | To Know rules of the game.                |')

        print('| Exit or Quit            | To Quit/Exit the game.                    |')

        print('-----------------------------------------------------------------------\n')

    elif input_1 == 'log' or input_1 == 'logs' or input_1 == 'db_load' or input_1 == 'stats':

        print('reading database...')

        time.sleep(2)

        read_log()

    elif input_1 == 'about':

        print('Hello,')

        print('      My self Tic-tac-toe and I was created by Vishal.')

        print('E-mail: 19vishalindustries@gmail.com')

    elif input_1 == 'exit' or input_1 == 'quit':

        exit()

    elif input_1 == 'start game' or input_1 == 'new game' or input_1 == 'game play' or input_1 == 'game start':

        duo_ai = input('Would you link to play with your friend or bot(f/b): ')

        if duo_ai == 'friend' or duo_ai == 'f' or duo_ai == 'my friend' or duo_ai == 'duo' or duo_ai == 'human':

            game_on = True

            print('Hello, I am A.I. robot and i am your umpire today.')

            u_name = input('What should i call you player 1(X)? ')

            u2_name = input('What should i call you player 2(O)? ')

            print("let's see who wins today.")

            print("let's start with the game now", u_name.upper(), 'vs', u2_name.upper(), '\n\n')

            print("Type 'Rule' to see Rules.")

            print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,

                  '|', 8, '|', 9, '\n')

            while game_on:

                command = int(input('>> Please enter the position you want to place the X to(1-9 only): '))

                check_game_x()

                print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',

                      r7, '|', r8, '|', r9, '\n')

                win_check()

                if win or tie:

                    write_log()

                    break

                command_2 = int(input('>> Please enter the position you want to place the O to(1-9 only): '))

                check_game_o()

                print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',

                      r7, '|', r8, '|', r9, '\n')

                win_check()

                if win or tie:

                    write_log()

                    break

        elif duo_ai == 'computer' or duo_ai == 'bot' or duo_ai == 'ai' or duo_ai == 'single' or duo_ai == 'b':

            print('Hello, I am A.I. robot and i am your opponent today.')

            u_name = input('What should i call you? ')

            print("let's see if you can beat me.")

            u2_name = 'bot'

            print("let's start with the game now", u_name.upper(), '\n\n')

            print("Type 'Rule' to see Rules.")

            print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,

                  '|', 8, '|', 9, '\n')

            game_on = True

            while game_on:

                command = int(input('>> Please enter the position you want to place the X to(1-9 only): '))

                check_game_x()

                print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',

                      r7, '|', r8, '|', r9, '\n')

                win_check()

                if win or tie:

                    write_log()

                    break

                print("It's my turn now")

                computer_turn()

                print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',

                      r7, '|', r8, '|', r9, '\n')

                win_check()

                if win or tie:

                    write_log()

                    break

    elif input_1 == 'rule' or input_1 == 'rules':

        rule()

    else:

        print("It's seems some error occurred, please check your spellings.")
