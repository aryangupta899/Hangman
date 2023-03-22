import random
import hangman_art


words = open(
    r'C:\Users\DELL\Desktop\python projects\HANGMAN\words.txt', "r")

content = words.read()
word_list = content.split("\n")

words.close()

list_length = len(word_list)
n = random.randint(0, list_length-1)

word = word_list[n]

# print(f'Pssst, the solution is {word}.')

print(hangman_art.logo)

blanks = ""
for i in word:
    blanks += '_'

print(blanks)

lives = 6
word_length = len(word)
while (blanks != word and lives > 0):
    guess = input("Guess a letter: ").lower()

    if word.find(guess) == -1:
        print("Incorrect guess, you lost a life")
        print(hangman_art.stages[lives])
        print("You have", lives, "remaining lives")
        lives -= 1
    else:
        for i in range(word_length):
            if word[i] == guess:
                print("You guessed a correct letter")
                blanks = blanks[:i] + guess + blanks[i+1:]

    print(blanks)

if lives == 0:
    print(hangman_art.stages[lives])
    print("Too bad, you lost")
    print("The word was:", word)
else:
    print("You won!")
