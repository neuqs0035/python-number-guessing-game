from random import randint

print("\n- - - - - - - - Number Guessing Game - - - - - - - - ")

while True:
    print("\n- - - - - - Main Menu - - - - - -")

    print("\n1 > Start Game")
    print("0 > Exit")

    main_menu_choice = int(input("\nEnter Choice : "))

    if(main_menu_choice == 1):
        
        print("\n-x -x -x -x -x -x -x -x Starting Game . . . . . . ")
        
        generated_num =  randint(0,100)
        tries = 0
        print(generated_num)
        while(True):
            print("\n1 > Guess The Number")
            print("0 > Exit Current Game")

            choice = int(input("\nEnter Choice : "))

            if(choice == 1):
                print("\nGuess The Number Between 0 TO 100")
                user_guess_num = int(input("\nEnter Guessed Number : "))
                tries += 1
                if(user_guess_num == generated_num):
                    print("\nYou Guessed It Right On ",tries," Tries , Congratulations -x -x -x -x -x -x -x -x")
                    break
                elif(user_guess_num < generated_num):
                    print("\nBigger Than Guessed Number , " , tries , " Tries . . . . .")
                else:
                    print("\nSmaller Than Guessed Number , " , tries , " Tries . . . . .")
            elif(choice == 0):
                print("\nThe Number Is " , generated_num , "\nExited Current Game . . . . . . .")
                break
            else:
                print("\nInvalid Input , Please Enter Correct Input Choice")
    elif(main_menu_choice == 0):
        print("\nProgram Exited . . . . . . .")
        break
    else:
        print("\nInvalid Input , Enter Valid Choice Number. . . . . . .")