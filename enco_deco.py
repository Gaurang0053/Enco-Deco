import random

result = ''
choice = ''
message = ''

characters_in_order = [chr(x) for x in range(32, 127)]

while choice != 0:

    choice = input(
        "\n Do you want to encrypt or decrypt the message?\n 1 to encrypt\n 2 to decrypt\n 0 to exit program.\n ")

    if str(choice) == '1':
        print("Hello MIT CELL:")
        message = input('\nEnter message for encryption: ')

        shift = input('Enter k value to shift transform message: ')
        random.seed(shift)
        shuffled_list = [chr(x) for x in range(32, 127)]
        random.shuffle(shuffled_list)

        for i in range(0, len(message)):
            result += shuffled_list[characters_in_order.index(message[i])]

        print(result + '\n\n')
        result = ''

    elif str(choice) == '2':
        print("Hello Instructor:")
        message = input('\nEnter message to decrypt: ')

        shift = input('To read this in original please type k value provided by the cell: ')
        random.seed(shift)
        shuffled_list = [chr(x) for x in range(32, 127)]
        random.shuffle(shuffled_list)

        for i in range(0, len(message)):
            result += characters_in_order[shuffled_list.index(message[i])]

        print(result + '\n\n')
        result = ''

    elif str(choice) != '0':
        print('You have entered an invalid input, please try again. \n\n')
    exit()
