import random
rock='''
    ___
---'    ___)
       (__)
       (__)
----   (___)
    '_(_)
    '''
paper='''

    ____
----'   __)___
           ___)
           ____)
           ___)
-----'______)
'''

scissors='''
    ____
---'    _)_
            ___)
        ___)
       (___)
---' _(__)

'''
game_images=[rock,paper,scissors]

user_choice=int(input("what do you choose? Type 0 for rock,1 for paperor 2 for scissors.\n"))
print(game_images[user_choice])
computer_choice= random.randint(0,2)
print("computer_choose:")
print(game_images[computer_choice])
if user_choice>=3 or user_choice<0:
    print("You typed an invalid number,you lose!")
elif user_choice==0 and computer_choice==2:
    print("You wins!")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice>user_choice:
    print("You lose!")
elif computer_choice<user_choice:
    print("You win!")
elif computer_choice==user_choice:
    print("It's draw") 
