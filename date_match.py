#! python3
# Written by Donna MacLeod, Sept 2018
# date_match.py - matches dates with regex format: Thursday, September 20, 2018
# \w+.\d+,.\d{4} matches August 7, 2018
# \w?\w?\w?\w{3}day,.\w+.\d+,.\d{4} matches Wednesday, August 7, 2018


import re 
source = open('./texts/text-with-dates.txt')    
text = source.read()
#print(text[:1000]) # prints the first 1000 characters of the file
print()

text_dates = re.findall('\w?\w?\w?\w{3}day,.\w+.\d+,.\d{4}', text) 
print(text_dates)

