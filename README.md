# Hangman Game

A polished, multi-screen Hangman game built with Python and CustomTkinter. Supports both random word mode and a custom multiplayer mode where Player 1 sets the word for Player 2 to guess.

---

## Features

- **Random Word Mode** — fetches a word from an online API with a local backup list
- **Custom Word Mode** — Player 1 enters a secret word, passes the device to Player 2
- **Hangman ASCII art** that progressively draws as you lose lives
- **Colour-coded letter buttons** — green for correct, red for wrong
- **Lives display** with heart indicators
- **Keyboard support** — type letters directly instead of clicking
- **Word definitions** shown on the result screen (fetched from Dictionary API)
- **Full game loop** — Play Again, New Game, Main Menu, and Exit from every screen

---

## Project Structure

```
hangman/
│
├── main.py          # App entry point and screen switching
├── screens.py       # All UI screens (MainMenu, GameScreen, ResultScreen, etc.)
├── game_logic.py    # Core game rules — guessing, win/lose checks, lives
├── word_source.py   # Random word fetching + dictionary definition lookup
├── requirements.txt # Python dependencies
└── README.md
```

---

## Setup & Installation

**Requirements:** Python 3.8+

1. Clone the repository
   ```bash
   git clone https://github.com/YOUR_USERNAME/hangman-game.git
   cd hangman-game
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game
   ```bash
   python main.py
   ```

---

## How to Play

### Random Word Mode
1. Launch the game and click **Play**
2. Select **Random Word**
3. Guess letters by clicking the on-screen buttons or typing on your keyboard
4. You have **6 lives** — each wrong guess draws more of the hangman
5. Win by guessing the full word before running out of lives

### Custom Word Mode (Multiplayer)
1. Click **Play** → **Custom Word**
2. Player 1 types a secret word (hidden with `***`)
3. Click **Start Game** — a "Pass the Device" screen appears
4. Player 1 hands the device to Player 2
5. Player 2 clicks **Start Guessing** and tries to guess the word

---

## Dependencies

| Package | Purpose |
|---|---|
| `customtkinter` | Modern dark-mode GUI framework |
| `requests` | Fetching random words and definitions from APIs |

Install with:
```bash
pip install customtkinter requests
```

---

## 🌐APIs Used

| API | Usage |
|---|---|
| [random-word-api.herokuapp.com](https://random-word-api.herokuapp.com) | Fetching a random word |
| [dictionaryapi.dev](https://dictionaryapi.dev) | Fetching the word's definition |

Both APIs have fallbacks — the game works fully offline using a built-in word list, and shows "definition unavailable" if the dictionary API can't be reached.

---

## Screens Overview

| Screen | Description |
|---|---|
| `MainMenu` | Title screen with Play and Exit |
| `PlayMenu` | Choose between Random Word or Custom Word |
| `CustomWordScreen` | Player 1 enters a secret word with show/hide toggle |
| `PassDeviceScreen` | Transition screen before Player 2 starts guessing |
| `GameScreen` | Main gameplay — letters, hangman art, lives |
| `ResultScreen` | Win/Lose screen with word, definition, and replay options |

---

## Built With

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)