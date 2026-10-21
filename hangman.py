import random

MAX_MISTAKES = 6

STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def load_words(filename="words.txt"):
    """Read words from the file, keeping only words with 4+ letters."""
    try:
        with open(filename, "r") as f:
            words = [w.strip().lower() for w in f
                     if w.strip().isalpha() and len(w.strip()) >= 4]
        if words:
            return words
    except FileNotFoundError:
        print("words.txt not found, using the built-in word list.")
    return ["python", "hangman", "internship", "computer", "keyboard", "program"]


def display_word(word, guessed):
    """Return the masked word, e.g. 'p _ t h _ n'."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def get_guess(guessed):
    """Ask for a valid, new single letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print("You already guessed that letter. Try another.")
        else:
            return guess


def play():
    words = load_words()
    word = random.choice(words)
    guessed = set()
    mistakes = 0

    print("== HANGMAN ==")

    while mistakes < MAX_MISTAKES:
        print(STAGES[mistakes])
        print("\nWord:", display_word(word, guessed))
        print("Guessed:", " ".join(sorted(guessed)) or "-")
        print(f"Mistakes left: {MAX_MISTAKES - mistakes}\n")

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            mistakes += 1
            print("Wrong guess!")

       
        if all(letter in guessed for letter in word):
            print("\n" + display_word(word, guessed))
            print("Congratulations, you won!")
            return

   
    print(STAGES[MAX_MISTAKES])
    print(f"\nGame over! The word was: {word}")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()