#! python3
# rex1.py - regex searching of text

import re 
source = open('./texts/pride&prejudice.txt')    
pride = source.read()
print(pride[:1000]) # prints the first 1000 characters of the file
print()

result = re.findall('[aeiou]', pride)  # finds all lowercase vowels in file and puts them into a single list
print('There are ' + str(len(result)) + ' lowercase vowels in Pride and Prejudice.')
print()

result = re.findall('[AEIOUaeiou]', pride)  # puts all vowels in file into a single list
print('There are ' + str(len(result)) + ' vowels in Pride and Prejudice.')
print()

print(result[:20])
print()

quotes = re.findall('"[^"]*r\n\r\n|"[^"]*"', pride) # puts all text inside "---" into a single list
print('There are ' + str(len(result)) + ' lowercase quotes in Pride and Prejudice.')
print()

print("This is quotes: ")
print(quotes[:10])
print()

quotes2 = quotes
print("This is quotes2: ")
print(quotes2[:10])
print()

pride_percent_quotes = len('"'.join(quotes2)) / float(len(pride)) *100
print("Quotes make up " + str(pride_percent_quotes) + "% of Pride and Prejudice.")
