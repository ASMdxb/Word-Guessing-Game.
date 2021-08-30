import random

name = input("What is your name?")

print ('Good Luck', name)

words = ['Wolf','Dog', 'Cat', 'House', 'Brother', 'Sister', 'Mother',
'Father', 'Kitchen', 'Television']

word = random.choice(words)

print ('Guess the Characters.')

guesses = ''

turns = 10

while turns >0:

    failed = 0

    for char in words:

        if char in guesses:
            
            print (char)

        else:
            print ('_')

        failed += 1

        if failed == 0:
            print('You Win!')

            print('The word is:', word)

            break

        guess = input('Guess a Character:')

        guesses += guess

        if guess not in word:

            turns -= 1

            print('You are Wrong!')

        print("You Have", + turns, "more guesses")

        if turns == 0:
            print('You Lose!')



            

