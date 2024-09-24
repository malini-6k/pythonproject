import random # module for randomly choose the values
from collections import Counter # Counter is a sub-class that is used to count hashable objects.

Words = '''ubuntu, windows, mac, python, pearl, java, c++, C, Keyboard, Mouse,Monitor, apple, orange, banana'''

Words = Words.split(' ')

word = random.choice(Words)# randomly choice from  "someWords" LIST.

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a Programming language')

    for i in word:

        print('_', end=' ')# printing the empty spaces
    print()

    playing = True

    letterGuessed = ''# the letters guessed by the player
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:  # Flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue


            if not guess.isalpha():# Validation
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue


            if guess in word:# If letter is guessed correctly

                k = word.count(guess)# k stores the number of times the guessed letter occurs in the word
                for _ in range(k):
                    letterGuessed += guess  # The guessed letter is added as many times as it occurs

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')


        if chances <= 0 and (Counter(letterGuessed) != Counter(word)): # If user has used all of his chances
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
