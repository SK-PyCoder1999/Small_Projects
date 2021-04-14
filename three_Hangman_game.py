import random
def Hangman():
    # making predifine list
    lst=['tiger','superman','thor','pokemon','honest','savewater','intelligent','animal']
    word=random.choice(lst)
    # making instructions
    valid_letters='abcdefghijklmnopqrstuvwxyz'
    total_turns=10
    Guess_made=""
    turns_left=total_turns
    while len(word) > 0 :
        main_word=""
        # checking the words
        for letter in word:
            if letter in Guess_made:
                main_word = main_word + letter
            else:
                main_word = main_word + "_" + " "
                
        if main_word == word :
            print(main_word)
            print("You have won the game !!")
            print("Right now, the Most happiest person is the Hangman.")
            print(" ------- ")
            print("  |_0_|  ")
            print("    |    ")
            print("   / \   ")
            break
            
        print("Guess the word: ", main_word)
        guess=input()
        if guess in valid_letters:
            Guess_made+=guess    
        else:
            print("Please enter only valid character ('a' to 'z')")
            guess=input()
            
        # reducing the turns
        if guess not in word:
            turns_left-=1
            # generating the figure
            if turns_left == 9 :
                print("9 turns are left")
                print(" ------- ")
            elif turns_left == 8 :
                print("8 turns are left")
                print(" ------- ")
                print("    0    ")  
            elif turns_left == 7 :
                print("7 turns are left")
                print(" ------- ")
                print("    0    ")
                print("    |    ")
            elif turns_left == 6 :
                print("6 turns are left")
                print(" ------- ")
                print("    0    ")
                print("    |    ")
                print("   /   ")
            elif turns_left == 5 :
                print("5 turns are left")
                print(" ------- ")
                print("    0    ")
                print("    |    ")
                print("   / \   ")
            elif turns_left == 4 :
                print("4 turns are left")
                print(" ------- ")
                print("   \0    ")
                print("    |    ")
                print("   / \   ")
            elif turns_left == 3 :
                print("3 turns are left")
                print(" ------- ")
                print("   \0/   ")
                print("    |    ")
                print("   / \   ")
            elif turns_left == 2 :
                print("2 turns are left")
                print(" ------- ")
                print("   \0/|  ")
                print("    |    ")
                print("   / \   ")
            elif turns_left == 1 :
                print("1 turn is left, rope is hanged")
                print("You have last chance to save a life of a kind man")
                print(" ------- ")
                print("   \0_|/ ")
                print("    |    ")
                print("   / \   ")
            elif turns_left == 0 :
                print("No turns are left")
                print("You have lost the game And letting a kinded man die.")
                print(" ------- ")
                print("    0_|  ")
                print("   /|\   ")
                print("   / \   ")
                break
                
# making interface
name=input("Please enter your name : ")
print("welcome",name,"!!")
print("------------------------------")
print("Now try to guess the word in less than 10 tries.")
Hangman()