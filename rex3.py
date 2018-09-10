#! python3
# rex3.py - regex searching of text, words

import re 
source = open('./texts/pride&prejudice.txt')    
pride = source.read()
print(pride[:1000]) # prints the first 1000 characters of the file
print()
print("-----------------------------NEXT BOOK-----------------------------------")

source = open('./texts/leavesOfGrass.txt')    
grass = source.read()
print(grass[:1000]) # prints the first 1000 characters of the file
print()

print("Calculation using the string method 'split'.")
pride_words = pride.split()  # defines word as anything between whitespaces, hyphened = 1 word
print("   There are " + str(len(pride_words)) + " words in Pride and Prejudice.")

grass_words = grass.split()
print("   There are " + str(len(grass_words)) + " words in Leaves of Grass.")

print()

print("Calculation using a regex for letters only.")
pride_words_2 = re.findall('[a-zA-Z]+', pride) # defines words as only letters, hyphenated & apostrophe = 2 words
print("   There are " + str(len(pride_words_2)) + " words in Pride and Prejudice.")
grass_words_2 = re.findall('[a-zA-Z]+', grass) 
print("   There are " + str(len(grass_words_2)) + " words in Leaves of Grass.")

print()

print("Slice from Pride and Prejudice: ")
print(pride_words_2[4000:4050])
print()
print("Slice from Leaves of Grass: ")
print(grass_words_2[4000:4050])
