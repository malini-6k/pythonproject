#importing the random module for select a random option by a system
import random

print("....Welcome to the ROCK PAPER SCISSOR game.... \n")
print("Winning rules for the ROCK PAPER SCISSOR GAME \n"
      + "Rock+Paper--> Paper Wins \n"
      + "Rock+Scissor--> Rock Wins \n"
      + "Paper+Scissor-->Scissor Wins\n")
while True:
    print("Enter your choice \n 1.Rock \n 2.Paper \n 3.Scissor \n")
    choice =int(input("Enter your Choice:"))

    while choice>3 or choice<1:
        choice=int(input("Enter a valid choice please :) \n"))

    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else:
        choice_name='Scissors'

    print("User choice: ",choice_name)
    print("Its Computers Turn...")

    comp_choice=random.randint(1,3)
    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissors'

    print("Computer choice:", comp_choice)
    print(choice_name, "vs", comp_choice_name)
    if choice == comp_choice:
        result="DRAW"
    elif (choice ==1 and comp_choice==2) or (comp_choice==1 and choice==2):
        result= "PAPER WINS"
    elif (choice==1 and comp_choice==3) or (comp_choice==1 and choice==3):
        result="ROCK WINS"
    else:
       result="SCISSOR WINS"

    if result=="DRAW":
        print("<-- It is Tie:) -->")
    elif result== choice_name:
        print("<-- User Wins -->")
    else:
        print("<-- Computer Wins -->")

    print("Do you want to PLAY AGAIN:(Yes/No) \n")
    ans= input().lower()
    if ans=='no':
        break
print("Well played :)  Thanks for Playing...")