import random

# Constants
INITIAL_GUESSES = 8

# Function to choose a random word from a list
def get_word():
    word_list = ["HAPPY", "PYTHON", "GUESS", "WORD", "GAME"]
    return random.choice(word_list)

# Function to play the game
def play_game(secret_word):
    guessed_word = ['-'] * len(secret_word)
    guesses_left = INITIAL_GUESSES
    
    while True:
        print("The word now looks like this:", ''.join(guessed_word))
        print("You have", guesses_left, "guesses left")
        guess = input("Type a single letter here, then press enter: ").upper()
        
        if len(guess) != 1:
            print("Guess should only be a single character.")
            continue
        
        if guess in secret_word:
            print("That guess is correct.")
            # Update guessed_word with the correctly guessed letter
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("There are no", guess + "'s in the word")
            guesses_left -= 1
        
        if '-' not in guessed_word:
            print("Congratulations, the word is:", secret_word)
            break
        
        if guesses_left == 0:
            print("Sorry, you lost. The secret word was:", secret_word)
            break

# Main function
def main():
    secret_word = get_word()
    play_game(secret_word)

# Run the game
if __name__ == '__main__':
    main()
