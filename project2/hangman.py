import random
def chooseRandomWord():
    words = ["WHDSPQZ" ,"XHO", "TTDBFRT", "QQJYF", "ENQD", "DNPK", "CNTR", "EHWHOD", "TSVMOHOF", "XNOCFQGTM"]
    ranNum = random.randint(0, len(words)-1)
    ranWord = words[ranNum]
    return ranWord

def getArrayOfLines(word):
    txt = ""
    for i in range (0, len(word)):
        txt = txt + " " + "-"
         
    return txt

def checkLetterBoolean(word, letters):
    for i in range (0, len(word)):
        if word[i] in letters[len(letters)-1]:
            return True
            
    return False 

def checkLetter(word, letters):
    line = ""
    for char in word: 
        if char in letters:
            line += " " + str(char)
        else:
            line += " " + "-"
    return line

def decrypt(word):
    originalword = ""
    for i in range (0, len(word)):
        if i % 2 == 0:
            plain_ascii = word[i]
            cipher_ascii = ord(plain_ascii)-1
            originalword = originalword + str(chr(cipher_ascii))
        else: 
            plain_ascii = word[i]
            cipher_ascii = ord(plain_ascii)+1
            originalword = originalword + str(chr(cipher_ascii))
            
    return originalword

def lettersToString(lst):
    to_return = ""
    for char in lst:
        to_return += " " + str(char)
        
    return to_return

def checkDuplicates(letters, letter):
    check = False
    if letter in letters:
        check = True 
    
    return check

def removeSpaces(word):
    return word.replace(" ", "") 

def main():
    total_lives = 10
    get_word = chooseRandomWord()
    line_word = getArrayOfLines(get_word)
    letters_guessed = ""
    letters = []
    check = False 
    while(total_lives > 0):
        print("You have " + str(total_lives) + " lives left and you have used these letters: " + letters_guessed)
        print("Current word: " + line_word)
        letter = input("Guess a letter: ").upper()
        if checkDuplicates(letters, letter) == False:
            letters.append(letter)
        else: 
            letter = input("Guess another letter, you guessed that already: ").upper()
            letters.append(letter)
        letters_guessed = lettersToString(letters)
        if checkLetterBoolean(get_word, letters) == False:
            total_lives = total_lives - 1
        else: 
            line_word = checkLetter(get_word, letters)
            
        if removeSpaces(line_word) == get_word:
            print("Yay! You guessed the word!")
            print("Here is the word you guessed: "+ get_word)
            print("This was an encrypted message!")
            print("The decoded message says: " + decrypt(get_word))
            break
        
        
    if total_lives == 0:
                print("No! You couldnt guess the word :( ")
                print("The word you couldn't guess was: " + get_word)
                print("Better luck next time!")

main()
