#Jayda Fountain
'''
This program is a game for the user in which they have to guess the
correct word. The user gets 6 guesses to find the correct 5 letter
word. When a letter is correct and in the right spot, a checkmark shows
up. When a letter is correct but in the wrong place, a reverse sign
shows up. When the letter is completely wrong, an X shows up. If the
user runs out of guesses, they lose. But if they guess the correct word
within the 6 guesses, they win.
'''
#Setting up the correct word
CORRECT_WORD = "climb"
word_list = list(CORRECT_WORD)

#Variables I need later on
guess_count = 0
correct_guess = True
output = []
winner = False

#Heading
print("WORDLE                                        Total Guesses: " + str(6))
print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")

#A while true loop to keep the program running until
#the user runs out of guesses
while True:
    #This function is called to get the user's input
    def user_guess():
        global guess
        
        #The user inputs their guess, and it's made into a list
        guess = input("Your guess: ")
        guess = guess.lower()
        guess_list = list(guess)
        
        #If there is too many letters, the user must re-input their guess
        while len(guess_list) > len(word_list):
            print("Too many letters, please input a 5 letter word.")
            guess = input("Your guess: ")
            guess_list = list(guess)
            
        check_guess(guess_list)
        
    #This function is called to decide if the user's guess is right        
    def check_guess(guess_list):
        num_char = 0
        index = 0
        
        #This for loop sorts through the user's guess list to see
        #whether or not each character is correct or wrong
        for char in range(len(guess_list)):
            #check if char at this index is correct
            if(guess_list[char] == word_list[index]):
                output.append("✅")
            #check if char at this index is anywhere else in the word
            elif(guess_list[char] in word_list):
                if(guess_list.count(guess_list[char]) > word_list.count(guess_list[char])):
                    if(num_char == 0):
                        output.append("❌")
                    elif(num_char >= 1):
                        output.append("🔄")
                    num_char += 1
                elif(guess_list.count(guess_list[char]) == word_list.count(guess_list[char])):
                    output.append("🔄")
                elif(guess_list.count(guess_list[char]) < word_list.count(guess_list[char])):
                    output.append("🔄")
            #char does not match anything
            else:
                output.append("❌")
            
            
            index += 1

        #Formatting
        print("       ")
        print("              ".join(output))
        print("       ")
        if(5 - guess_count != 0):
            print("Guesses Left: " + str((5 - guess_count)))
            print("-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
        
    
    user_guess()

    #The user wins
    if(guess == CORRECT_WORD):
        winner = True
        print("You guessed it right!")
        break
    
    #Reset the output list after each guess
    output = []
    
    #Augment the number of guesses after each guess
    guess_count += 1
    
    #The user loses
    if(guess_count >= 6):
        winner = False
        print("GAME OVER!")
        print("The correct word is " + CORRECT_WORD)
        break