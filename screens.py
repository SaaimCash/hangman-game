import customtkinter as ctk
import string

from word_source import get_random_word, get_definition
from game_logic import HangmanGame



# MAIN MENU SCREEN

class MainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title_label = ctk.CTkLabel(self, text="HANGMAN", font=("Arial", 48, "bold"))
        title_label.pack(pady=80)

        play_button = ctk.CTkButton(
            self,
            text="Play",
            width=200,
            height=50,
            font=("Arial", 24),
            command=self.go_to_play_menu
        )
        play_button.pack(pady=20)

        exit_button = ctk.CTkButton(
            self,
            text="Exit",
            width=200,
            height=50,
            font=("Arial", 24),
            fg_color="#C0392B",
            hover_color="#96281B",
            command=master.quit
        )
        exit_button.pack(pady=20)

    def go_to_play_menu(self):
        self.master.clear_screen()
        self.master.current_screen = PlayMenu(self.master)
        self.master.current_screen.pack(fill="both", expand=True)



# PLAY MENU SCREEN

class PlayMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title_label = ctk.CTkLabel(self, text="Choose Game Mode", font=("Arial", 40, "bold"))
        title_label.pack(pady=60)

        random_button = ctk.CTkButton(
            self,
            text="🎲  Random Word",
            width=250,
            height=55,
            font=("Arial", 22),
            command=self.start_random_game
        )
        random_button.pack(pady=15)

        custom_button = ctk.CTkButton(
            self,
            text="✏️  Custom Word",
            width=250,
            height=55,
            font=("Arial", 22),
            command=self.start_custom_game
        )
        custom_button.pack(pady=15)

        back_button = ctk.CTkButton(
            self,
            text="Back",
            width=250,
            height=45,
            font=("Arial", 20),
            fg_color="gray40",
            hover_color="gray25",
            command=self.go_back
        )
        back_button.pack(pady=40)

    def start_random_game(self):
        random_word = get_random_word()
        self.master.clear_screen()
        self.master.current_screen = GameScreen(self.master, random_word, mode="random")
        self.master.current_screen.pack(fill="both", expand=True)

    def start_custom_game(self):
        self.master.clear_screen()
        self.master.current_screen = CustomWordScreen(self.master)
        self.master.current_screen.pack(fill="both", expand=True)

    def go_back(self):
        self.master.show_main_menu()



# CUSTOM WORD SCREEN

class CustomWordScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.word_visible = False

        title_label = ctk.CTkLabel(self, text="Enter Custom Word", font=("Arial", 36, "bold"))
        title_label.pack(pady=40)

        instruction_label = ctk.CTkLabel(
            self,
            text="Player 1: Type a secret word for Player 2 to guess.",
            font=("Arial", 16),
            text_color="gray70"
        )
        instruction_label.pack(pady=(0, 20))

        self.word_entry = ctk.CTkEntry(
            self,
            width=300,
            height=50,
            font=("Arial", 24),
            show="*",
            placeholder_text="Secret word..."
        )
        self.word_entry.pack(pady=10)
        self.word_entry.bind("<Return>", lambda e: self.start_game())

        # Error Label
        self.error_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 16),
            text_color="#E74C3C"
        )
        self.error_label.pack(pady=5)

        self.toggle_button = ctk.CTkButton(
            self,
            text="👁  Show Word",
            width=160,
            height=36,
            font=("Arial", 16),
            fg_color="gray40",
            hover_color="gray25",
            command=self.toggle_word_visibility
        )
        self.toggle_button.pack(pady=8)

        start_button = ctk.CTkButton(
            self,
            text="Start Game",
            width=200,
            height=50,
            font=("Arial", 22),
            command=self.start_game
        )
        start_button.pack(pady=20)

        back_button = ctk.CTkButton(
            self,
            text="Back",
            width=200,
            height=40,
            font=("Arial", 18),
            fg_color="gray40",
            hover_color="gray25",
            command=self.go_back
        )
        back_button.pack(pady=10)

    def toggle_word_visibility(self):
        if self.word_visible:
            self.word_entry.configure(show="*")
            self.toggle_button.configure(text="👁  Show Word")
            self.word_visible = False
        else:
            self.word_entry.configure(show="")
            self.toggle_button.configure(text="🙈  Hide Word")
            self.word_visible = True

    def start_game(self):
        custom_word = self.word_entry.get().strip().lower()

        if not custom_word:
            self.error_label.configure(text="Please enter a word.")
            return

        if not custom_word.isalpha():
            self.error_label.configure(text="Only letters allowed — no spaces or symbols.")
            return

        if len(custom_word) < 2:
            self.error_label.configure(text="Word must be at least 2 letters.")
            return

        self.error_label.configure(text="")

        self.master.clear_screen()
        self.master.current_screen = PassDeviceScreen(self.master, custom_word)
        self.master.current_screen.pack(fill="both", expand=True)

    def go_back(self):
        self.master.clear_screen()
        self.master.current_screen = PlayMenu(self.master)
        self.master.current_screen.pack(fill="both", expand=True)



# PASS DEVICE SCREEN

class PassDeviceScreen(ctk.CTkFrame):
    def __init__(self, master, custom_word):
        super().__init__(master)

        self.custom_word = custom_word

        ctk.CTkLabel(
            self,
            text="🤝",
            font=("Arial", 64)
        ).pack(pady=(80, 10))

        ctk.CTkLabel(
            self,
            text="Pass the device to Player 2",
            font=("Arial", 36, "bold")
        ).pack(pady=10)

        ctk.CTkLabel(
            self,
            text="Player 1's word has been saved.\nDon't let Player 2 see the screen!",
            font=("Arial", 16),
            text_color="gray70",
            justify="center"
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="▶  Start Guessing",
            width=250,
            height=55,
            font=("Arial", 24),
            command=self.start_game
        ).pack(pady=40)

        ctk.CTkButton(
            self,
            text="Back",
            width=200,
            height=40,
            font=("Arial", 18),
            fg_color="gray40",
            hover_color="gray25",
            command=self.go_back
        ).pack(pady=5)

    def start_game(self):
        self.master.clear_screen()
        self.master.current_screen = GameScreen(self.master, self.custom_word, mode="custom")
        self.master.current_screen.pack(fill="both", expand=True)

    def go_back(self):
        self.master.clear_screen()
        self.master.current_screen = CustomWordScreen(self.master)
        self.master.current_screen.pack(fill="both", expand=True)



# GAME SCREEN

class GameScreen(ctk.CTkFrame):

    HANGMAN_PICS = [
        """
 -----
 |   |
     |
     |
     |
     |
=========""",
        """
 -----
 |   |
 O   |
     |
     |
     |
=========""",
        """
 -----
 |   |
 O   |
 |   |
     |
     |
=========""",
        """
 -----
 |   |
 O   |
/|   |
     |
     |
=========""",
        """
 -----
 |   |
 O   |
/|\\  |
     |
     |
=========""",
        """
 -----
 |   |
 O   |
/|\\  |
/    |
     |
=========""",
        """
 -----
 |   |
 O   |
/|\\  |
/ \\  |
     |
========="""
    ]

    def __init__(self, master, word, mode="random"):
        super().__init__(master)

        self.word = word
        self.mode = mode  # "random" or "custom" — used by ResultScreen for replay
        self.game = HangmanGame(word)
        self.letter_buttons = {}  # dict: letter -> button

        # Bind keyboard input
        self.master.bind("<Key>", self.handle_keypress)

        # ---- Layout ----

        # Top row: hangman art + word/lives side by side
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(pady=(15, 0), fill="x", padx=30)

        # Hangman art (left)
        self.hangman_label = ctk.CTkLabel(
            top_frame,
            text=self.HANGMAN_PICS[0],
            font=("Courier", 16),
            justify="left"
        )
        self.hangman_label.pack(side="left", padx=(20, 40))

        # Right side: title, word, lives, status
        right_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        right_frame.pack(side="left", fill="both", expand=True)

        ctk.CTkLabel(right_frame, text="HANGMAN", font=("Arial", 32, "bold")).pack(pady=(20, 10))

        self.word_label = ctk.CTkLabel(
            right_frame,
            text=self.game.get_display_word(),
            font=("Courier", 34, "bold"),
            text_color="#3498DB"
        )
        self.word_label.pack(pady=10)

        self.lives_label = ctk.CTkLabel(
            right_frame,
            text=self._lives_text(),
            font=("Arial", 20)
        )
        self.lives_label.pack(pady=5)

        self.status_label = ctk.CTkLabel(
            right_frame,
            text="",
            font=("Arial", 16),
            text_color="#E67E22"
        )
        self.status_label.pack(pady=4)

        # Divider
        ctk.CTkFrame(self, height=2, fg_color="gray30").pack(fill="x", padx=20, pady=10)

        # Letter buttons grid
        letters_frame = ctk.CTkFrame(self, fg_color="transparent")
        letters_frame.pack(pady=10)

        for index, letter in enumerate(string.ascii_lowercase):
            btn = ctk.CTkButton(
                letters_frame,
                text=letter.upper(),
                width=50,
                height=40,
                font=("Arial", 15, "bold"),
                command=lambda l=letter: self.guess_letter(l)
            )
            row = index // 9
            col = index % 9
            btn.grid(row=row, column=col, padx=3, pady=3)
            self.letter_buttons[letter] = btn

        # Bottom button row: Main Menu + Exit
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(pady=(8, 4))

        ctk.CTkButton(
            bottom_frame,
            text="🏠  Main Menu",
            width=180,
            height=38,
            font=("Arial", 15),
            fg_color="gray40",
            hover_color="gray25",
            command=self._go_to_main_menu
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            bottom_frame,
            text="Exit",
            width=180,
            height=38,
            font=("Arial", 15),
            fg_color="#C0392B",
            hover_color="#96281B",
            command=self.master.quit
        ).pack(side="left", padx=10)

    def _go_to_main_menu(self):
        self.master.unbind("<Key>")
        self.master.show_main_menu()

    def _lives_text(self):
        hearts = "❤️" * self.game.remaining_lives()
        return f"Lives: {hearts}  ({self.game.remaining_lives()} left)"

    def handle_keypress(self, event):
        """Handle physical keyboard input."""
        key = event.char.lower()
        if key in string.ascii_lowercase:
            self.guess_letter(key)

    def guess_letter(self, letter):
        # Repeat guess — flash warning, do nothing else
        if letter in self.game.guessed_letters:
            self.status_label.configure(text=f"'{letter.upper()}' already guessed!")
            return

        self.status_label.configure(text="")

        # Process guess — get result back from game logic
        result = self.game.guess_letter(letter)

        # Color the button based on correct / wrong
        btn = self.letter_buttons[letter]
        if result == "correct":
            btn.configure(state="disabled", fg_color="#27AE60", text_color="white")
        else:
            btn.configure(state="disabled", fg_color="#C0392B", text_color="white")

        # Update hangman drawing
        self.hangman_label.configure(text=self.HANGMAN_PICS[self.game.wrong_guesses])

        # Update word display
        self.word_label.configure(text=self.game.get_display_word())

        # Update lives
        self.lives_label.configure(text=self._lives_text())

        # Check end conditions
        if self.game.is_winner():
            self._end_game(won=True)
        elif self.game.is_loser():
            self._end_game(won=False)

    def _end_game(self, won):
        # Unbind keyboard so it doesn't fire on the next screen
        self.master.unbind("<Key>")

        # Fetch definition (may return None if API unavailable)
        definition = get_definition(self.word)

        # Capture final hangman drawing to show on loss screen
        final_hangman = self.HANGMAN_PICS[self.game.wrong_guesses]

        self.master.clear_screen()
        self.master.current_screen = ResultScreen(
            self.master, won, self.word, self.mode,
            definition=definition, hangman_pic=final_hangman
        )
        self.master.current_screen.pack(fill="both", expand=True)



# RESULT SCREEN

class ResultScreen(ctk.CTkFrame):
    def __init__(self, master, won, word, mode="random",
                 definition=None, hangman_pic=""):
        super().__init__(master)

        self.word = word
        self.mode = mode

        if won:
            # ── WIN LAYOUT ──────────────────────────────────────────
            ctk.CTkLabel(
                self,
                text="🎉 YOU WON!",
                font=("Arial", 44, "bold"),
                text_color="#2ECC71"
            ).pack(pady=(40, 10))

            # Word reveal
            ctk.CTkLabel(
                self,
                text=word.upper(),
                font=("Courier", 36, "bold"),
                text_color="#3498DB"
            ).pack(pady=(0, 6))

            # Definition
            self._add_definition(definition)

            self._add_buttons(master)

        else:
            # ── LOSE LAYOUT ──────────────────────────────────────────
            ctk.CTkLabel(
                self,
                text="💀 YOU LOST!",
                font=("Arial", 44, "bold"),
                text_color="#E74C3C"
            ).pack(pady=(30, 10))

            # Middle row: hangman art (left) + word & definition (right)
            middle_frame = ctk.CTkFrame(self, fg_color="transparent")
            middle_frame.pack(fill="x", padx=40, pady=10)

            # Hangman art
            ctk.CTkLabel(
                middle_frame,
                text=hangman_pic,
                font=("Courier", 15),
                justify="left"
            ).pack(side="left", padx=(10, 40), anchor="n")

            # Right side: word + definition
            right_frame = ctk.CTkFrame(middle_frame, fg_color="transparent")
            right_frame.pack(side="left", anchor="n", pady=10)

            ctk.CTkLabel(
                right_frame,
                text="The word was:",
                font=("Arial", 18),
                text_color="gray70"
            ).pack(anchor="w")

            ctk.CTkLabel(
                right_frame,
                text=word.upper(),
                font=("Courier", 34, "bold"),
                text_color="#E74C3C"
            ).pack(anchor="w", pady=(0, 10))

            self._add_definition(definition, parent=right_frame)

            self._add_buttons(master)

    def _add_definition(self, definition, parent=None):
        """Render the definition label, or a fallback if unavailable."""
        parent = parent or self

        if definition:
            # Wrap long definitions — split roughly at 60 chars
            wrapped = self._wrap_text(definition, 62)
            ctk.CTkLabel(
                parent,
                text=wrapped,
                font=("Arial", 15),
                text_color="gray80",
                justify="left",
                wraplength=520
            ).pack(anchor="w", pady=(0, 10))
        else:
            ctk.CTkLabel(
                parent,
                text="(definition unavailable)",
                font=("Arial", 14),
                text_color="gray50",
                justify="left"
            ).pack(anchor="w", pady=(0, 10))

    @staticmethod
    def _wrap_text(text, width):
        """Simple word-wrap to keep definition readable."""
        words = text.split()
        lines, current = [], []
        length = 0
        for w in words:
            if length + len(w) + 1 > width:
                lines.append(" ".join(current))
                current, length = [w], len(w)
            else:
                current.append(w)
                length += len(w) + 1
        if current:
            lines.append(" ".join(current))
        return "\n".join(lines)

    def _add_buttons(self, master):
        """Shared button row for both win and lose screens."""
        ctk.CTkFrame(self, height=2, fg_color="gray30").pack(fill="x", padx=20, pady=12)

        ctk.CTkButton(
            self,
            text="▶  Play Again",
            width=260,
            height=50,
            font=("Arial", 21),
            command=self.play_again
        ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="🎲  New Game",
            width=260,
            height=45,
            font=("Arial", 19),
            fg_color="gray40",
            hover_color="gray25",
            command=self.go_to_play_menu
        ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="🏠  Main Menu",
            width=260,
            height=45,
            font=("Arial", 19),
            fg_color="gray40",
            hover_color="gray25",
            command=master.show_main_menu
        ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="Exit",
            width=260,
            height=42,
            font=("Arial", 17),
            fg_color="#C0392B",
            hover_color="#96281B",
            command=master.quit
        ).pack(pady=12)

    def play_again(self):
        self.master.clear_screen()
        if self.mode == "custom":
            self.master.current_screen = CustomWordScreen(self.master)
        else:
            new_word = get_random_word()
            self.master.current_screen = GameScreen(self.master, new_word, mode="random")
        self.master.current_screen.pack(fill="both", expand=True)

    def go_to_play_menu(self):
        self.master.clear_screen()
        self.master.current_screen = PlayMenu(self.master)
        self.master.current_screen.pack(fill="both", expand=True)