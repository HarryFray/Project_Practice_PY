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
        for vowel in 'aeiouAEIOU':
            if vowel == FirstLetter:
             PigString += word + 'yay '

        for con in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            if con == FirstLetter:
                vowelplace = []
                for vowel in 'aeiouAEIOU':
                    if word.find(vowel) == -1:
                        pass
                    else:
                        place = word.find(vowel)
                        vowelplace.append(place)
                        FirstVowelLocation = min(vowelplace)
                PigString += word[FirstVowelLocation:] + word[:FirstVowelLocation] + ' '
    print PigString

Rinput = raw_input('English to Pig Latin:')
print Rinput
PigLatin(Rinput)