class Game:
    ADVENTURE_OPTIONS = ""  \
        + "What would you like to do?" \
        + "\n\t[1] 🚀 look for wild pokemon!" \
        + "\n\t[2] 😡 battle a trainer! (bonus)" \
        + "\n\t[3] 🏥 heal my pokemon" \
        + "\n\t[4] 🔎 examine my pokemon " \
        + "\n\t[5] 💾 save" \
        + "\n\t[6] 👋 quit"

    def __init__(self):
        """Initialize a brand new game with a clean "game state"
        """

    def start(self):
        """After
        """

    def save(self):
        """Save game state as a .json file to "<player_name>.json" in whichever
        folder the pokequest.py python file was run from
        """
        pass

    def load(self):
        """Look for .json files in whichever folder the pokequest.py python file was run
        from. Assume any of these are valid.
        """
        pass