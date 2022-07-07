#----------------------------------------------------
# Task 3:The Wordle Game
# Purpose of program: design and implement the Wordle175 game while using the ScrabbleDict class
# Author: Priyanshu Pusola
# Collaborators/references: None
#----------------------------------------------------


import random 
from Wordle175 import ScrabbleDict
from clean import read_words
    
def check_input (user_input,prev_guess,dictionary):
   
   
   '''
        1.This function gets the WordSize from Wordle175
        2.Cheks the User input and compare it with word in dictionary
        3.Raises specific errors if the condition is not satisfied
        
        Inputs: user input and getWordSize()
        Returns: True or False depending on the condition
        
   '''   
   
   word_limit = dictionary.getWordSize()
   if word_limit > len(user_input):
      print(user_input.upper(), "is too short ")
      return False
   if word_limit < len(user_input):
      print(user_input.upper(), "is too long ")
      return False
   if user_input in prev_guess:
      print(user_input.upper(), "was already entered ")
      return False
   if not dictionary.check(user_input):
      print(user_input.upper(),"is not a recognized word")
      return False
   return True
            

def main():
   
   '''
        1.This main function intialises and plays the game
        2.Total number of attempts is 6
        3.Game ends when word is correctly guessed or attempts is more than 6
        4.Stores the user_input in a list (prev_guess) which checks if a word is already entered
        5.Adds the alphabets in respective sets of colour
        6.Picks a random word from txt file (scrabble5.txt)
        
        
        Inputs: check_input function and the dictionary (ScrabbleDict5)
        Returns: The Wordle Game !!
     
        
   ''' 
   
   
   word = 'rider'
   attempts = 1
   dictionary = ScrabbleDict(5, "scrabble5.txt")
   continue_game = True
   
   #Test to check if the random word is being picked or not 
   #print(word)
   while continue_game == True:
      prev_guess = []
      while continue_game == True:
         guess = input("ATTEMPT "+ str(attempts) +": Please enter a 5 five-letter word: ").lower()
         
         #creating sets of colour that would store the alphabets depending on each colour condition 
         if check_input(guess, prev_guess, dictionary):
            red = set()
            green = set()
            orange = set()
            letterCount = {}
            for i in range(len(guess)):
               letter = guess[i]
               lettern = letter
               if letter in letterCount:
                  lettern = letter + str(letterCount[letter] + 1)
                  letterCount[letter] += 1
               else:
                  letterCount[letter] = 1
                  
               #Specifying the colour set conditions
               if guess[i] == word[i]:
                     green.add(lettern)
               elif guess[i] in word and list(word).count(guess[i]) >= list(guess).count(guess[i]):
                     orange.add(lettern)
               else:
                     red.add(lettern)
                     
            #Win or Lose conditions
            if len(green) == 5:
               print('Found in' ,attempts,"attempt. Well done. The Word is" ,word.upper())
               return continue_game == False
            if attempts == 6:
               print("TRIAL ""GREEN = ", green,"ORANGE = ", orange,"RED = ", red)
               print('Sorry you lose. The Word is',word.upper())
               return continue_game == False
            
            #Displaying previous entered answers and the summary of colour sets
            else:
                  print(guess.upper() + " " + "Green = " + "{" + ",".join(green)+ "}" +" "+ "Orange = " "{"\
                         + ",".join(orange)+ "}" +" " + "Red = " + "{" + ",".join(red)+ "}")
                  attempts +=1
               
            prev_guess.append(guess)   
main()
