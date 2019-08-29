#!/usr/bin/env python
# coding: utf-8

# # Hello, welcome to the game of Mastermind
# 
# ### Mastermind game description and rules:
# 
# #### Users:
# 
# Codemaker: The code maker is the person who chooses a pattern of four code strings and provide feedback to the Codebreaker.
# 
# Codebraker: The codebreaker tries to guess the pattern, in both order and color, within twelve (or ten, or eight) turns.
# 
# #### The game is played using:
# 
# 1- A “decoding board” with a shield cover one of the ends of the board protecting the four code pegs created by the Codemaker and and twelve (or ten, or eight, or six) additional rows containing four large holes next to a set of four small holes.
# 
# 2- Code list of six different colors strings. [ ‘green’, ‘red’, ‘yellow’, ‘blue’, ‘purple’, ‘pink’ ]
# 
# 3- Key strings in a list, some “black” , some “white” .
# 
# #### The flow:
# 
# 1- The Codemaker creates the pattern which is a list of four elements (i.e. [ ‘green’, ‘red’, ‘yellow’, ‘red’ ] ). This is created by the computer and you will not be able to see it, it is hidden from you. 
# 
# 2- The Codebreaker decides the difficulty of the game by choosing how many rounds. More rounds increases the chances of winning the game by decoding the code. 
# 
# 3- The Codebreaker writes down the pattern for the first time (i.e. [ ‘red’, ‘yellow’, ‘purple’, ‘red’ ] ).
# 
# 4- The Codemaker provides feedback by returning a list of “black” and “whites” strings indicating:
# 
# 	4.1. “Black” means that you guess the color and the index of the element in the pattern but does not tell you which element. 
# 	4.2. “White” means that you guess the color but not the location but does not tell you which element. 
#     4.3. " - " means that the color is not part of the codomaker code. 
#     
# (i.e. [ ' - ', "white", ' - ', 'black' ] ).
# 
# 5 - Step 3 and 4 are repeated sequentially until the Codebreaker solve the code or the number of rounds reached the limit. 
# 
# 6- If the Codebreaker solve the code before the number of rounds then he wins, and if not, the Codemaker wins. 
# 

# In[1]:


# import library

import random
import sys
import time

# In[2]:


# Setting up the variables

color_list_options = ['RED', 'YELLOW', 'BLUE', 'GREEN', 'PINK', 'PURPLE']
level_rounds = { 'easy': 12, 'medium': 8, 'hard': 4} #Dictionary where keys are the difficulty levels and values are the rounds or trials to guess the codemaker pattern


# In[3]:


# DEFINING THE DIFFICULTY LEVEL THUS THE ROUNDS OF THE GAME
#By asking the codebreaker the difficulty level he or she wants to play.

# Easy = 12 rounds, Medium = 8 rounds and Hard = 4 rounds

def ask_user_difficulty_level():
    
    difficulty_level = input("Choose the difficult level (easy, medium or hard) for the game: \n").lower()
    
    if difficulty_level not in level_rounds.keys():
        print("\n FATAL ERROR: Your response must be 'easy', 'medium' or 'hard'. \n")
        sys.exit()
        
    else:
        return level_rounds[difficulty_level]
    

# In[4]:


# DEFINING THE CODEMAKER CODE PATTERN IN A RANDOM WAY

def codemaker_code_pattern():
    
    codemaker_code = random.sample(color_list_options, 4)
    return codemaker_code



# In[5]:


# DEFINING THE CODEBREAKER GUESS

def codebreaker_guess():
    
    print('\nThe game color options are: red, yellow, blue, green, pink and purple.\n')
      
    user_code_choice = input("Enter four colors separated by a SINGLE SPACE: \n").upper()
    
    user_choice  = user_code_choice.split()

    while any(item not in color_list_options for item in user_choice) == True or len(user_choice) != 4:
        user_code_choice = input("Try again: Enter four colors from the list separated by a SINGLE SPACE: \n").upper()
    
        user_choice  = user_code_choice.split()
        
    return user_choice



# In[6]:


# COMPARING THE CODEBREAKER GUESS WITH THE CODEMAKER CODE PATTERN.

def feedback_codemaker(pattern_maker, pattern_breaker):
    
    feedback = []
    
    for i in range(4):
        
        if pattern_breaker[i] == pattern_maker[i]:
            feedback.append('black')
            
        elif pattern_breaker[i] in pattern_maker:
            feedback.append('white')
        
        else:
            feedback.append(' - ')
            
    return sorted(feedback)
    

# In[7]:


# DEFINING THE GAME FLOW

def game():
    
    print('Welcome to the MASTERMIND game, please enjoy and follow the instructions, GOOD LUCK!!')
    
    time.sleep(1) #Gives one second of delay to run the "ROUNDS = ask_user_difficulty_level()"
    
    ROUNDS = ask_user_difficulty_level()
    
    print(f'\n You will play {ROUNDS} rounds \n ')
    print('--------------------------------------------------------------')
    
    CODEMAKER_PATTERN = codemaker_code_pattern()
    
    rounds_played = 1
    
    while rounds_played <= ROUNDS:
        
            code_breaker_guess = codebreaker_guess()
            
            print('\nYour guess is:')
            
            print(code_breaker_guess)

            rounds_played += 1

            feedback_list = feedback_codemaker(CODEMAKER_PATTERN,code_breaker_guess)
            
            print('\nYour feed back is: \n')

            print(feedback_list)
            
            print(f'\nThis was the round {rounds_played - 1} \n')
            
            print('-------------------------------------------------------')
            
            if CODEMAKER_PATTERN == code_breaker_guess:
                print('You won!!!!!!')
                break
        
    if rounds_played > ROUNDS:
        print("You loose, you run out of rounds!!!! Try another time")
        
        print(f" \nThe codemaker pattern was {CODEMAKER_PATTERN}")


# In[8]:


game()

# In[ ]:





# In[ ]:



