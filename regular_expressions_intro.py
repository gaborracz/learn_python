"""
    ^           - Matches the beginning of a line
    $           - Matches the end of the line
    .           - Matches any character
    \s          - Matches whitespace
    \S          - Matches any non-whitespace character
    *           - Repeats a character zero or more times
    *?          - Repeats a character zero or more times (non-greedy)
    +           - Repeats a character one or more times
    +?          - Repeats a character one or more times (non-greedy)
    [aeiou]     - Matches a single character in the listed se
    [^XYZ]      - Matches a single character not in the listed set
    [a-z0-9]    - The set of characters can include a range
    (           - Indicates where string extraction is to start
    )           - Indicates where string extraction is to end

    For more information about using regular expressions in Python, see https://docs.python.org/3/howto/regex.html
"""

import re

file_handler = open('mbox-short.txt')

for line in file_handler :
    line = line.rstrip()

    if re.search('From:', line) :
        print(line)

"""
    When we use re.findall() it returns a list of zero
    or more substrings that match the regular 
    expression.
"""

x = 'My 2 favoite numbers are 19 and 42'

y = re.findall('[0-9]+', x)

print(y)

"""
    The repeat characters * and + push outward
    in both directions (greedy) to match the
    largest possible string.
"""

x = "From: Using the : character"

y = re.findall('^F.+:' , x)

print(y)

"""
    Not all regular expression repeat codes are 
    greedy! If you add a ? character, the + and *
    chill out a bit...
"""

y = re.findall('^F.+?:' , x)

print(y)

"""
    You can define the match for re.findall() and separtely 
    determine which portion of the match is to be 
    extracte by usind parentheses.
"""

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('\S+@\S+', x)

print(y)

Y = re.findall('From (\S+@\S+)', x)

print(y)

y = re.findall('@([^ ]*)', x)

print(y)

y = re.findall('@(\S+)', x)

print(y)

"""
    Escape character: if you want a special reular expression
    to just behave normally (most of the time) you prefix it with \ character.
"""

x = 'We just received $10.00 for cookies.'

y = re.findall('\$[0-9]+', x)

print(y)