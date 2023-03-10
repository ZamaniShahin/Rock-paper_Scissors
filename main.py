from random import randint
'''
1 == rock
2 == paper
3 == scissor
'''

while(True):
    choice = input('Please Enter your choice(R/P/S/B(break))').lower()
    machine_choice = randint(1, 3)
    if (choice == 'e'):
        break;
    elif (choice == 'r' and machine_choice == 1):
        print('Draw!')
    elif (choice == 'r' and machine_choice == 2):
        print('you lost!')
    elif (choice == 'r' and machine_choice == 3):
        print('You win! Congrats.')
    elif (choice == 'p' and machine_choice == 1):
        print('You win! Congrats.')
    elif (choice == 'p' and machine_choice == 2):
        print('Draw!')
    elif (choice == 'p' and machine_choice == 3):
        print('You Lost!')
    elif (choice == 's' and machine_choice == 1):
        print('You Lost!')
    elif (choice == 's' and machine_choice == 2):
        print('You Win! Congrats.')
    elif (choice == 's' and machine_choice == 3):
        print('Draw!')
    else:
        print('Please Enter Correct Input!')