# in General

sentence = "Louis "
sentence += "is 21yrs old"
print(sentence)

# use placeholder
name = "Louis "
newSentence = "%s is 21 yrs old"
print(newSentence % name)
print(newSentence % "Jake ")

# multiple placeholders
multiplePlaceholder = "%s %s is my name"
print(multiplePlaceholder % ("Louis", "Leonardo"))

# Int placeholder
sentence = "%s is %d"
print(sentence % ("Louis", 21))
