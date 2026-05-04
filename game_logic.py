class HangmanGame:
    #iniatialized variables
    def __init__(self, word):
        self.selected_word = word.lower()
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.max_wrong = 6

   
    # Guess a Letter
    def guess_letter(self, letter):
        letter = letter.lower()

        # Ignore repeat guesses
        if letter in self.guessed_letters:
            return "repeat"

        self.guessed_letters.append(letter)

        if letter not in self.selected_word:
            self.wrong_guesses += 1
            return "wrong"

        return "correct"


    # Display Current Word
    def get_display_word(self):
        return " ".join(
            [letter if letter in self.guessed_letters else "_"
             for letter in self.selected_word]
        )

   
    # Win Check
    def is_winner(self):
        return all(letter in self.guessed_letters for letter in self.selected_word)

    # Lose Check
    def is_loser(self):
        return self.wrong_guesses >= self.max_wrong

    # Lives Left
    def remaining_lives(self):
        return self.max_wrong - self.wrong_guesses