
# HigherorLowerGame
HigherorLower Game setup in Python



**Introduction**
The player has to guess if the next card will be Higher or Lower as compared to the last card. For every correct answer, points are increased by 15, and for wrong guess the points are reduced by 10. The player will be given 100 points initially to start with.


**Description and Logic**
 - Major logic is written in three classes – Card, Deck, Game. All the final variables are defined in the Constants file and imported in all the classes and functions to be re-used.
	 - Class Card – Contains all the properties related to a Card
	 - Class Deck – Collection of Cards defined in step (a). Each Deck is collection of 52 cards, each card object having a face value and color associated to it
	 - Class Game – Uses the Deck Class with additional properties. e.g. When user clicks on New Game, Deck Class is shuffled and the points are reset.
 - I am using Library – “pygwidgets” written by Prof. Irv Kalb. This library is wrapper on collection of user interface widgets (e.g. buttons, frames, etc) written in Python. This takes care of building the complete user interface and refreshing it on user action. Details about this can by found at location https://pygwidgets.readthedocs.io/en/latest/
 - Concepts used in the included projects
	 - Classes   {Game.py}
	 - Functions   {Game.py, Main.py}
	 - Importing external modules   {Game.py}
	 - Data Structures – tuple   {CONSTANTS.py}
	 - User created iterators   {Game.py && Main.py}
	 - Error checks using try-except {Main.py}
	 - User Input {Main.py}
	 - Decorator @staticmethod  {Game.py}
