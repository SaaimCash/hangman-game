import requests
import random

# Backup local words if API fails — broad mix of difficulties
backup_words = [
    # Easy
    "cat", "dog", "sun", "hat", "map", "cup", "bed", "fox", "owl", "arm",
    # Medium
    "python", "hangman", "jungle", "planet", "bridge", "castle", "garden",
    "island", "rocket", "spider", "forest", "bottle", "silver", "frozen",
    # Hard
    "developer", "keyboard", "monitor", "computer", "champion", "jealousy",
    "alchemy", "labyrinth", "mystical", "universe", "adventure", "chocolate",
    "hurricane", "lightning", "telescope", "discovery", "celebrate", "carnival",
]


def get_random_word():
    try:
        response = requests.get(
            "https://random-word-api.herokuapp.com/word",
            timeout=3
        )
        if response.status_code == 200:
            word = response.json()[0].lower()
            if word.isalpha() and len(word) >= 3:
                return word
    except Exception:
        pass

    # Fallback to local list
    return random.choice(backup_words)


def get_definition(word):
    """
    Fetch the first definition of a word from the Free Dictionary API.
    Returns a string definition, or None if not found.
    """
    try:
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
            timeout=4
        )
        if response.status_code == 200:
            data = response.json()
            # Drill into the nested structure: entries → meanings → definitions
            meanings = data[0].get("meanings", [])
            if meanings:
                part_of_speech = meanings[0].get("partOfSpeech", "")
                definitions = meanings[0].get("definitions", [])
                if definitions:
                    definition = definitions[0].get("definition", "")
                    if definition:
                        return f"({part_of_speech})  {definition}"
    except Exception:
        pass

    return None