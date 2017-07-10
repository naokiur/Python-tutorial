# Example single quart
singleQuart = 'spam eggs'
print(singleQuart)

escapeSingleQuart = 'doesn\'t'
# If you use Mac with JIS keyboard, type option + ¥ for inputting \.
print(escapeSingleQuart)

escapeSingleQuartwithDouble = "doesn't"
print(escapeSingleQuartwithDouble)

escapeDouble = '"Yes", he said.'
print(escapeDouble)

escapeDoubleWithBackslash = "\"Yes\", he said."
print(escapeDoubleWithBackslash)

escapeBackslash = '"Isn\'t," she said.'
print(escapeBackslash)

print('C:\some\name')
print(r'C:\some\name')  # use raw String

print("""\
multiple row String exclude first line feed.
Usage: thingy [OPTIONS]
    -h          Display this usage message
    -H hostname Hostname to connect to
""")

print("""
multiple row String include first line feed.
Usage: thingy [OPTIONS]
    -h          Display this usage message
    -H hostname Hostname to connect to
""")

repeatedJoinString = 3 * 'un' + 'ium'
print(repeatedJoinString)

autoJoin = 'Py' 'thon'
print(autoJoin)

# Auto join is only literal
prefix = 'Py'
# print(prefix 'thon') this is compile error

joinVariable = prefix + 'thon'
print(joinVariable)

longSentence = ('Thank you for your answer. I think I understand this.'
                ' But I don\'t understand anther point.'
                ' So, I would like to ask something you.')

print(longSentence)

word = 'Python'
print(word[0]) # Character position is 0. So this is P.
print(word[5]) # Character position is 5. So this is n.
print(word[-1]) # Last character. So this is n.
print(word[-2]) # Second last character. So this is o.
print(word[-6]) # Sixth last character. So this is P.
print(word[0:2]) # Slice 0(include) to 2(exclude).
print(word[2:5]) # Slice 2(include) to 5(exclude).
print(word[:2] + word[2:]) # Always include begin index, exclude end index.
print(word[:4] + word[4:])
print(word[:])

# This is compile error because String is immutable.
# word[0] = 'J'

# Embedded function 'len()' will return length of String.
print(len(word))
