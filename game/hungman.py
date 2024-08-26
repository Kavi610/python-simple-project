import random

#1.Update a word list to use the 'word_lost'from word.py
from game.word import word_list
Choose_word=random.choice(word_list)
word_length=len(Choose_word)

#Create a variable called 'lives' to keep track  to the number of the lives left.

lives=6
end_of_game=False
#2.Imporet stagg from logo.py and make this error go away.
#from word import word_list

#3.Import the logo from logo.py
from game.logo import stages,hungman_logo
print(hungman_logo)
print(stages[lives])

#Create a empty list called Display
display=[]
for _ in range(word_length):
#Store the blank list in display value
    display += "_"
    
#Ask the user to guess a letter and design their answer toi a variable called guess.Make guess lowercase

while not end_of_game:
    guess=input("Guess a letter: ").lower()
    
#4  If user has entered a letter they have already guessed,print the letter and let them know.
    #Check guessed letter
    
    for position in range(len(Choose_word)):
        letter=Choose_word[position]
        print(f'current position:{position}\n current letter:{letter}\n guess letter:{guess}')
        if letter==guess:
            display[position]=letter
            
    #check if user is wrong.
    
    if guess not in Choose_word:
#5 If the letter is not in the choose_word ,print out the letter and let them know it's not in the word.
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")
            
    #join all the element in the list and turn it into a String.
    
    print(f"{''.join(display)}")
    
    #check if user has got all letter.
    
    if "_" not in display:
        end_of_game=True
        print("You win")
    


