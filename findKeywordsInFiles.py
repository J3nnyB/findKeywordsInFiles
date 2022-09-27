"""
Jennifer Byrne, Sept 27, 2022
Python script - 3 functions: 
    print_directory - lists files in a directory
    search_file - searches for a word in a file
    search_directory - searches for a word in a directory/folder
"""
import os

# function lists files in a directory
def print_directory(directory_path):
    # files variable is the directory named in the absolute path 
    files = os.listdir(directory_path)
    # prints this message 
    print('These are the files found in', directory_path)
    for file in files:
        print(file) # prints all of the files found in the named directory

# function searches for a word (passed parameter) in a file
def search_file(file_path, word):
    # opens file as readable using the passed parameter file_path
    with open(file_path, 'r') as file:
        # reads file
        content = file.read()
        # counts word in the read file
        word_count = content.count(word)
        if word in content:
            # if the word is in the read file,
            # prints the file being searched and how many times the word was found
            print('Searching in', file_path)
            print('Word was found in file this many times:', word_count)
        else:
            # if the word isn't in the read file,
            # prints this message 
            print('Word does not exist in this directory.') 

# function searches for a word (passed parameter) in a directory/folder
def search_directory(folder_path, word):
    # file pathway
    for files in os.listdir(folder_path):
        # opens each file
        with open(os.path.join(folder_path, files), 'r') as file:
            # reads each file
            content = file.read()
            # counts word in each read file
            word_count = content.count(word)
            if word in content:
                # if word is found,
                # prints out file name and how many times the word was found
                print('Searching in', file.name)
                print('Word was found in file this many times:', word_count)
            else:
                # if word isn't in the file,
                # prints this message
                print('Word does not exist in', file.name)

# calls print_directory function and passes this file path as a parameter    
print_directory('C:\projects\PracticeTestScripts\PyTextFiles')
# calls search_file function and passes this file path and word as parameters
search_file(r'C:\projects\PracticeTestScripts\PyTextFiles\test1.txt', 'tortor')
# calls search_directory function and passes this directory path and word as parameters
search_directory(r'C:\projects\PracticeTestScripts\PyTextFiles', 'tortor')