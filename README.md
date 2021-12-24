# flashcardGenerator
a widget to create flashcard decks
- the widget sticks to the top for easier access when working with multiple windows
- has configurable variables for things like naming files and delimiting front/back entries
- validation to prevent blank entries or delimiters present the front/back entries themselves
- supports utf-8 characters
- example use-case: i use this to generate flashcard decks to import into Anki

<img src="./img/preview.jpg" width="100%" height="auto">

-----

## Usage
1) run 'flashcards.pyw', this should bring up a GUI window

<img src="./img/step_1.JPG" width="80%" height="auto">

2) enter the front and back values for the flashcard as indicated by the input labels

<img src="./img/step_2.JPG" width="80%" height="auto">

3) click the "Add Card" button to add the card to the session

<img src="./img/step_3.JPG" width="80%" height="auto">

4) repeat steps 2 and 3 as needed to add cards to the session

<img src="./img/step_4.JPG" width="80%" height="auto">

5) when finished adding cards, click "Save"; this should generate a flashcards file and output the filename

<img src="./img/step_5.JPG" width="80%" height="auto">

6) navigate to the "decks" folder to view the generated flashcard files

<img src="./img/step_6.JPG" width="80%" height="auto">

7) the flashcard files should contain the card entries that were entered during the session with the front and back delimited (in this case the delimited is a colon ":" character)

<img src="./img/step_7.JPG" width="80%" height="auto">

(extra) to configure additional settings, one can modify the variables at the start of the script

<img src="./img/step_8.JPG" width="80%" height="auto">
