import random
#this method will choose a random word from the arrray of word that we have using random.randint to choose
#a number between 0 and the last index in the array 
#it returns the word that is chosen 
def chooseRandomWord():
    words = ["WHDSPQZ" ,"XHO", "TTDBFRT", "QQJYF", "ENQD", "DNPK", "CNTR", "EHWHOD", "TSVMOHOF", "XNOCFQGTM"]
    ranNum = random.randint(0, len(words)-1)
    ranWord = words[ranNum]
    return ranWord

#this method gets the correct amount of dashses that spans the length of the word that was chosen 
def getArrayOfLines(word):
    txt = ""
    for i in range (0, len(word)):
        txt = txt + " " + "-"
         
    return txt

#checks if the recently entered letter exists in the word that we are trying to guess
#if it exists then we return true otherwise we return false 
def checkLetterBoolean(word, letters):
    for i in range (0, len(word)):
        if word[i] in letters[len(letters)-1]:
            return True
            
    return False 


#this method returns the current word with any correct letters that were guessed by the user
#if any of the letter that were guessed correctly by the user exist in the word itself then it prints that character
#for any letters that arent guessed yet it prints out a dashed - 
def checkLetter(word, letters):
    line = ""
    for char in word: 
        if char in letters:
            line += " " + str(char)
        else:
            line += " " + "-"
    return line

#this method decrypts the word that the user guessed 
#if the current index is even then we take the ASCII value of that char and subtract one and concatnate it to a string
#if the current index is odd then we take the ASCII value of that char and add one and concatnate it to a string
#we return the decrypted word 
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

#since we use an array to keep track of the guessed letters
#this method just takes that array of letters and turns it into a string to display it to the user
def lettersToString(lst):
    to_return = ""
    for char in lst:
        to_return += " " + str(char)
        
    return to_return

#this method just checks to see if the recently entered letter has already been guessed by the user 
#once the user guesses one letter it can no longer input that letter again 
#so if the letter passed in exists in our letters array then we return true otherwise we return false 
def checkDuplicates(letters, letter):
    check = False
    if letter in letters:
        check = True 
    
    return check

#since the word that is guessed is displayed with spaces, we remove the spaces to check if the user has guessed 
#the word correctly
def removeSpaces(word):
    return word.replace(" ", "") 

#handles the main logic and overall game 
def main():
    total_lives = 10
    get_word = chooseRandomWord()
    line_word = getArrayOfLines(get_word)
    letters_guessed = ""
    letters = []
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
