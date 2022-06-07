'''
have characters list
    maybe made from 
        unmodified keys
        shift keys
        altgr keys

main menu:
    1 play if list not empty
    2 add unmod to list
    3 add shift to list
    4 add altgr to list
    5 quit

play:
    randomize list order
    loop while list not empty:
        ask for char in list, if correct remove from list
       
'''
import random

unmod = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',
         'p', '[', ']', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm',
         ',', '.', '/']
shift = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O',
         'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
         '<', '>', '?']
altgr = []

main_menu_text = "1: PLAY\n2: Add UNMOD\n3: Add SHIFT \n4: Add ALTGR\n5: RESET\n6: QUIT\n"


def main():
    chosen = []
    play = False
    while not play:
        user_input = input(main_menu_text)
        match int(user_input):
            case 1:
                play = True
            case 2:
                chosen += unmod
                play = False
            case 3:
                chosen += shift
                play = False
            case 4:
                chosen += altgr
                play = False
            case 5:
                chosen.clear()
                play = False
            case 6:
                exit()
            case _:
                play = False

    while len(chosen) > 0:
        random.shuffle(chosen)
        answer = input(chosen[0] + '\n')
        if answer == chosen[0]:
            chosen.pop(0)
            print('CORRECT')
        elif answer == "quit":
            print('QUIT')
            exit()
        else:
            print('INCORRECT')


main()
