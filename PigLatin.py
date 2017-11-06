''' The rules used by Pig Latin are as follows:
If a word begins with a vowel, just as "yay" to
the end. For example, "out" is translated into "outyay".
If it begins with a consonant, then we take all consonants
before the first vowel and we put them on the end of the word.
'''
def PigLatin(string):
    list = string.split()
    PigString = ''
    for word in list:
        FirstLetter = word[0]
        for vowel in 'aeiou':
            if FirstLetter == vowel:
                PigString += word + 'yay '
    print PigString




PigLatin('bite apple julia is real smart sometimes lol octagon')