import random
import ast

file = open('dictionary.txt','r')

contents = file.read()
wordLists = ast.literal_eval(contents)

file.close()


unKnownWords = {}
powerOff = True

def randomWord(word):

    while powerOff:

        words = random.choice(list(wordLists.keys()))
        print(words)

        
        def dictionary(word):
            global powerOff
            global wordLists
            global unKnownWords

            inPut = input('> ')

            if inPut == 'exit':
                powerOff = False
            
            elif inPut == wordLists[word]:
                print()
                pass

            else:
                print('False')
                print()
                if wordLists[word] not in unKnownWords:
                    unKnownWords[words] = wordLists[word]
                    
            return unKnownWords

        wrongWords = dictionary(words)

    return wrongWords

print(30 * '= ')

print('Stopping Program enter - > exit')

print(30 * '= ')
print()

unknownWordList = randomWord(wordLists)


print(f'\nYou must review these words {unknownWordList}')
