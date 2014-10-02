def root(x):
    guess = float(x/2)
    while abs(x - guess*guess) > 0.001:
    	quotient = x / guess
        guess = (guess + quotient) / 2
    print guess
#root(100)

def numberToWord(number, wordList, mapping):
    sevenLetterWords = generate(number, mapping)
    print sevenLetterWords
    result = []

    # 3 and 4
    threeFourLeft = []
    threeFourRight = []

    # 4 and 3
    fourThreeLeft = []
    fourThreeRight = []

    for word in sevenLetterWords:
        if word[:3] in wordList:
                threeFourLeft.append(word[:3])
          	if word[3:] in wordList:
				threeFourRight.append(word[3:])
        if word[:4] in wordList:
            fourThreeLeft.append(word[:4])
        if word[4:] in wordList:
            fourThreeRight.append(word[4:])
        if word in wordList:
            result.append(word)
     
    for word3 in threeFourLeft:
        for word4 in threeFourRight:
            result.append(word3 + word4)

    for word3 in fourThreeLeft:
        for word4 in fourThreeRight:
            result.append(word3 + word4)

    return result

def generate(number, mapping):
    if len(number) <= 0:
        return []
    results = []
    suffix = generate(number[1:], mapping)
    for letter in mapping[number[0]]:
        for s in suffix:
            results.append(letter + s)
    return results

mapper = { "2": "ABC", "3": "DEF", "4":"GHI", "5":"JKL", "6":"MNO"}
words = {"BAD", "DEF", "CAD", "BED", "FAD", "BEE", "FEE", "FEED", "ABC"}

print numberToWord("2223333", words, mapper)