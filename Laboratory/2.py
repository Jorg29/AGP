#2)Write a program that displays for the string "How I need a drink alcoholic of course, after all those lectures involving quantum mechanics" the number of characters of each word.

import re
string="How I need a drink alcoholic of course, after all those lectures involving quantum mechanics"
print("How I need a drink alcoholic of course, after all those lectures involving quantum mechanics")
res = len(re.findall(r'\w+', string))
print("The number of Characters in string are : ", len(string))
