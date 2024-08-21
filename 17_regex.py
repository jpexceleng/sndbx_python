# 1 Introduction
# ----------------------------------------------------------------------------
"""
Regex (Regular Expressions) are sequences of characters that define a search
pattern. They're powerful for text processing tasks like searching, extracting,
or replacing text.

Basic Concepts

    Literal characters: 
    Characters like a, 1, or @ match themselves.
    
    Meta-characters:
    Characters with special meanings, e.g., ., *, +, ?, ^, $, [, ], {, }, |, \.

"""

# 2 Using the 're' module
# ----------------------------------------------------------------------------
#Python's re module provides functions to work with regex.
import re

# 2.1 Common Functions
# ----------------------------------------------------------------------------
# Search for a pattern within a string. Returns a match object if found, else None.
match = re.search(r'\d+', 'abc123')
if match:
    print(match.group())  # Output: 123

# Find all occurrences of a pattern in a string and returns them as a list.
numbers = re.findall(r'\d+', 'abc123def456')
print(numbers)  # Output: ['123', '456']

# Check if the pattern matches the start of the string.
match = re.match(r'abc', 'abcdef')
if match:
    print(match.group())  # Output: abc

# Split a string by the occurrences of the pattern.
parts = re.split(r'\d+', 'abc123def456')
print(parts)  # Output: ['abc', 'def', '']

# Replace occurrences of a pattern with a replacement string.
result = re.sub(r'\d+', '#', 'abc123def456')
print(result)  # Output: abc#def#

# 3 Regex Syntax
# ----------------------------------------------------------------------------
# 3.1 Common Meta-characters

#.: Matches any character except a newline.
print(re.findall(r'a.c', 'abc a c aXc'))  # Output: ['abc', 'aXc']

#^: Matches the start of a string.
print(re.findall(r'^abc', 'abcdef abc'))  # Output: ['abc']

#$: Matches the end of a string.
print(re.findall(r'abc$', 'defabc'))  # Output: ['abc']

#*: Matches 0 or more repetitions of the preceding pattern.
print(re.findall(r'ab*c', 'abc ac abbbc'))  # Output: ['abc', 'ac', 'abbbc']

#+: Matches 1 or more repetitions of the preceding pattern.
print(re.findall(r'ab+c', 'abc ac abbbc'))  # Output: ['abc', 'abbbc']

#?: Matches 0 or 1 repetition of the preceding pattern.
print(re.findall(r'ab?c', 'abc ac abbc'))  # Output: ['abc', 'ac']

#[]: Matches any character inside the brackets.
print(re.findall(r'a[bc]d', 'abd acd abcd'))  # Output: ['abd']

#|: Matches either the pattern before or after the |.
print(re.findall(r'abc|def', 'abcdef'))  # Output: ['abc', 'def']

#(): Groups patterns and captures the matched text.
match = re.search(r'(abc)(def)', 'abcdef')
if match:
    print(match.group(1))  # Output: abc
    print(match.group(2))  # Output: def
    
# 3.2 Escape Characters

# Use \ to escape meta-characters or specify special sequences like \d for
# digits, \w for word characters, etc.

# \d matches digits, \w matches word characters (alphanumeric + underscore)
print(re.findall(r'\d+', 'abc123def456'))  # Output: ['123', '456']
print(re.findall(r'\w+', 'abc 123 def'))   # Output: ['abc', '123', 'def']


# 4 Advanced Features
# ----------------------------------------------------------------------------
# 4.1 Lookahead and Lookbehind

#Positive Lookahead ((?=...)): Ensures that what follows the current position matches the pattern but does not consume characters.
print(re.findall(r'\w+(?=\d)', 'abc123 def456'))  # Output: ['abc', 'def']

#Negative Lookahead ((?!...)): Ensures that what follows does not match the pattern.
print(re.findall(r'\w+(?!\d)', 'abc123 def456'))  # Output: ['def']

#Positive Lookbehind ((?<=...)): Ensures that what precedes the current position matches the pattern.
print(re.findall(r'(?<=\d)\w+', '123abc 456def'))  # Output: ['abc', 'def']

#Negative Lookbehind ((?<!...)): Ensures that what precedes does not match the pattern.
print(re.findall(r'(?<!\d)\w+', '123abc def456'))  # Output: ['def']

# 4.2 Non-capturing Groups

#    Use (?:...) for non-capturing groups, which groups the pattern without capturing the match.
match = re.search(r'(?:abc)(def)', 'abcdef')
if match:
    print(match.group(1))  # Output: def