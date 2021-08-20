import random
import ast

file = open('vocabluary.txt','r',encoding="utf8",errors='ignore')

contents = file.read()
wordLists = ast.literal_eval(contents)

file.close()


unKnownWords = {}
powerOff = True
newWord = []
count = 0

def randomWord(word):
    
    global count
    
    while powerOff:

        words = random.choice(list(wordLists.keys()))
                
        if words not in newWord:
            count = count + 1
            print(count,'.',words)
            
                
            
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
                print(wordLists[word])
                print()
                if wordLists[word] not in unKnownWords:
                    unKnownWords[words] = wordLists[word]
                    
            return unKnownWords
        
        wrongWords = dictionary(words)
        onlyKeys = wrongWords.values()
             

    return onlyKeys



print(30 * '= ')

print('Stopping Program enter - > exit')

print(30 * '= ')
print()

unknownWordList = randomWord(wordLists)
converToListObj = list(unknownWordList)


print(f'\nYou must review these words {converToListObj}')
