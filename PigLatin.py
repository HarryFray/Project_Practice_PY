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
        vowels = 'aeiouAEIOU'
        if FirstLetter in vowels:
             PigString += word + 'yay '
        else:
            ''' use (not in) or (in) here to simplify code '''
            vowelplace = []
            for vowel in vowels:
                if word.find(vowel) == -1:pass
                    # FirstVowelLocation = [0]
                else:
                     place = word.find(vowel)
                     vowelplace.append(place)
                     FirstVowelLocation = min(vowelplace)
            PigString += word[FirstVowelLocation:] + word[:FirstVowelLocation] + ' '
    print PigString

Rinput = raw_input('English to Pig Latin:')
print Rinput
PigLatin(Rinput)