#! python3
# rex1.py - regex searching of text

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


pride_quotes = re.findall('"[^"]*r\n\r\n|"[^"]*"', pride) # puts all text inside "---" into a single list
print('There are ' + str(len(pride_quotes)) + ' lowercase quotes in Pride and Prejudice.')
print()

grass_quotes = re.findall('"[^"]*r\n\r\n|"[^"]*"', grass) # puts all text inside "---" into a single list
print('There are ' + str(len(grass_quotes)) + ' lowercase quotes in Leaves of Grass.')
print()

print("Pride quotes: ")
print(pride_quotes[:10])
print()
print("Grass quotes: ")
print(grass_quotes[:10])
print()

pride_percent_quotes = len('"'.join(pride_quotes)) / float(len(pride)) *100
print("Quotes make up " + str(pride_percent_quotes) + "% of Pride and Prejudice.")
grass_percent_quotes = len('"'.join(grass_quotes)) / float(len(grass)) *100
print("Quotes make up " + str(grass_percent_quotes) + "% of Leaves of Grass.")
