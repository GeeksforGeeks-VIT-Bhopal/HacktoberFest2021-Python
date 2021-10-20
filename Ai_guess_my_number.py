def main():
    print('think of a number between 0 and 100')
    min_value = 0
    max_value = 100

    while True:
        query = min_value + (max_value - min_value) // 2
        if check_is_answer(query):
            # you know you have the right answer
            break
        if check_is_greater(query):
            # you know the number must be greater than query
            min_value = query + 1
        else:
            # you know the number must be less than query
            max_value = query - 1
    print('Your number was ', query)


def check_is_answer(value):
    return ask_true_false('Is your number '+str(value)+'?')


def check_is_greater(value):
    return ask_true_false('Is your number greater than '+str(value)+'?')


def ask_true_false(prompt):
    response = input(prompt + ' (y/n) ')
    return response == 'y' or response == 'Y'


if __name__ == "__main__":
    main()
