def main():
        rounds=1
        computerScore=0
        playerScore=0
        winner={"computer","nobody","player"}
        print("********************** * Rock Paper Scissors * ***********************")
        while rounds<=5 :
                from random import randint
                #printing the menu for the user
                print("Current Scores:",'\n', "Computer score:" , computerScore, '\n', "Player score:", playerScore)
                print("——"*10)
                print("Round",rounds)
                print("——"*5)
                print("It’s your turn, the computer has chosen. It’s time to make your choice.",'\n',"-R for Rock",'\n',"-P for Paper",'\n',"-S for Scissors")
                USER_INPUT=str(input("Please choose an option:"))
                while USER_INPUT not in {"R", "r","P", "p","S", "s"}:
                    USER_INPUT=str(input("This is not an option in the menu.Please choose a valid option:"))
                COMPUTER_INPUT=randint(0,3)
                #converting the input to integers option
                if USER_INPUT=="R" or USER_INPUT=="r":
                    USER_INPUT=0
                elif USER_INPUT=="P" or USER_INPUT=="p":
                    USER_INPUT=1
                elif USER_INPUT=="S" or USER_INPUT=="s":
                    USER_INPUT=2
                if COMPUTER_INPUT=="R" or COMPUTER_INPUT=="r":
                    COMPUTER_INPUT=0
                elif COMPUTER_INPUT=="P" or COMPUTER_INPUT=="p":
                    COMPUTER_INPUT=1
                elif COMPUTER_INPUT=="S" or COMPUTER_INPUT=="s":
                    COMPUTER_INPUT=2
                #comparing the inputs and deciding who wins
                if USER_INPUT == 0 and COMPUTER_INPUT == 0:
                    print("Player chose: rock!")
                    print("Computer chose:rock!")
                    print("Draw" )
                    winner="nobody"

                elif USER_INPUT == 0 and COMPUTER_INPUT == 1:
                    print("Player chose: rock!")
                    print("Computer chose: paper!")
                    print("Computer wins this round! Paper covers rock")
                    winner="computer"

                elif USER_INPUT == 0 and COMPUTER_INPUT == 2:
                    print("Player chose: rock!")
                    print("Computer chose: scissors!")
                    print("Player wins this round! Rock blunts Scissors")
                    winner="player"

                elif USER_INPUT == 1 and COMPUTER_INPUT == 0:
                     print("Player chose: paper!")
                     print("Computer chose: rock!")
                     print("Player wins this round! Paper covers rock" )
                     winner="player"

                elif USER_INPUT==1 and COMPUTER_INPUT == 1:
                     print("Player chose: paper!")
                     print("Computer chose: paper!")
                     print("Draw")
                     winner="nobody"

                elif USER_INPUT==1 and COMPUTER_INPUT == 2:
                     print("You chose: paper!")
                     print("Computer chose: scissors!")
                     print("Computer wins this round! Scissors cuts paper")
                     winner="computer"

                elif USER_INPUT == 2 and COMPUTER_INPUT==0:
                     print("Player chose: scissors!")
                     print("Computer chose: rock!")
                     print("Computer wins this round! Rock blunts scissors" )
                     winner="computer"

                elif USER_INPUT == 2 and COMPUTER_INPUT == 1:
                     print("Player chose: scissors!")
                     print("Computer chose: paper!")
                     print("Player wins this round! Scissors cut paper")
                     winner="player"

                elif USER_INPUT == 2 and COMPUTER_INPUT == 2:
                      print("Player chose: scissors!")
                      print("Computer chose: scissors!")
                      print("Draw")
                      winner="nobody"

                if winner=="computer":
                        computerScore=computerScore+1
                elif winner=="player":
                        playerScore=playerScore+1
                else:
                        computerScore=computerScore
                        playerScore=playerScore

                rounds=rounds+1
                an=playerScore-computerScore
                bn=computerScore-playerScore

                if an==3 or bn==3 :
                        break
                if rounds==5 and(an==2 or bn==2):
                        break
               
        print("")
        print("Final outcome")
        print("Computer", computerScore)
        print("Player", playerScore)
        if computerScore>playerScore:
                print("The computer wins!")
        elif computerScore==playerScore:
                print("Draw!")

        else:
                print("The player wins!")


main()
                



            



