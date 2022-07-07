# Task 1
# Creates a new text file from corrupted word5Dict.txt
# Author : Priyanshu Pusola

def read_words(input_file):
        
        new_dict= []
        with open('word5Dict.txt','r') as f:
                for line in f:
                        for word in line.split('#'):
                                new_dict.append(word)                       
        return new_dict
                                
def print_new_file(input_file,new_dict):                        
        with open(input_file, 'w') as dictionary:
                dictionary.write('\n'.join(new_dict))

def main():
        print_new_file('scrabble5.txt', read_words('word5Dict.txt'))
main()