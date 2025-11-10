import re

text = "Their phone numer is 1234567890 and their name " \
"is jeff. Jeff's wifes phone number is (930)-345-7866 and her name " \
"is sarah. "

#The pattern that I will be trying to locate and extract.
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'

#Finding all the values that matches the inputted pattern(s).
matches = re.findall(pattern, text)

print(matches)