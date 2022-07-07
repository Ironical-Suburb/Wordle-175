#----------------------------------------------------
# Task 2: Files Containing all the Classes
# Purpose of program: class file with the necessary classes
# Author: Priyanshu Pusola
# Collaborators/references: None
#----------------------------------------------------

class ScrabbleDict:
    
    def __init__(self, size, filename):
        
        '''
        1.This function initialises the new created class (ScrabbleDict)
        2.Opens Scrabble5Dict.txt
        3.Creates the new dictionary from the file Scrabble5Dict.txt
        
        Inputs: word file ('Scrabble5Dict.txt')
        Returns: New Created Dictionary (" self.dictionary ")
        
        '''        
        
        self.dictionary = {}
        self.size = size 
        self.filename = filename
        with open(filename, 'r') as file:
            lines = file.readlines()
            new_list = []
            for element in lines:
                new_list.append(element.strip())
            for x in new_list:
                first_element = x
                for alphabet in x:
                    z = first_element[0]
                if len(x) == self.getWordSize():
                    self.dictionary[x] = z

    def check(self,word):
        
        '''
        Checks if the word guessed by user is in the dictionary
        
        Inputs: word in dictionary ('Scrabble5Dict.txt')
        Returns: True - word in dictionary
                 False - word not in dictionary
        
        ''' 
        
        if word in self.dictionary:
            return True 
        else :
            return False
    
    def getSize(self):
        
        '''
        Returns the numbers of words in the dictionary 
        
        Inputs: word in dictionary ('Scrabble5Dict.txt')
        Returns: size of the dictionary / number of words in dictionary
        
        '''
        
        return len(self.dictionary)
    
    def getWords(self,letter):
        l=[]
        for x in self.dictionary: 
            if x[0]==letter.lower():
                l.append(x)
                l = sorted(l)
        return (l)           

        
    def getWordSize(self):
        
        '''
        1.Returns size of each individual word
        2.Size of each word is 5
        
        Inputs: words in dictionary ('Scrabble5Dict.txt')
        Returns: size of each individual word
        
        '''
        
        return self.size
        
# Tests for the Above Code:
if __name__ == "__main__":
    
    print( "Creating ScrabbleDict with size as 5 and file = 'scrabble5.txt' from clean.py" )
    dictionary = ScrabbleDict(5,'scrabble5.txt')
    
    # Test for check function
    print("1."f" aunty returns True. Return: {dictionary.check('aunty')}" )
    print( "2."f" music returns True. Return: {dictionary.check('music')}" )
    print("3." f" soccer returns False. Return: {dictionary.check('soccer')}" )
    print( "4."f" bazar returns True. Return: {dictionary.check('bazar')}" )

    # Test for size function
    print( f"Size of dictionary :-  {dictionary.getSize()} words" )

    # Test for getWord function 
    print( "Sorted words starting with 'x'" )
    print( dictionary.getWords('x') )
    print( "Sorted words starting with 't'" )
    print( dictionary.getWords('t') )

    # Test for Word Size function
    print( f'The Word size for dictionary :- {dictionary.getWordSize()} letters' )


    