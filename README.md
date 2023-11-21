Higher/Lower - Movie Edition

This is a game of Higher/Lower where the user guesses which movie has a higher rating among two randomly selected from a
database. When the user starts the app, they need to enter a nickname, which must be a single word (without spaces) and
cannot be empty. After entering the nickname, a menu opens, offering options to start the game, view existing high
scores, or quit the app. The high score system only saves the top 10 scores, along with the user's nickname who achieved
them. If the user's nickname is 'admin,' the menu expands to include additional options such as checking the entire
movie list in the database, editing a movie selected by ID, and adding a new movie. All interactions are performed
within the app.

All inputs are protected from common errors. For instance, during admin editing or adding, inputs like names cannot be
empty. Conditions for inputs like the year include being a 4-symbol string consisting of integers and starting with '
18,' '19,' or '20' to validate the year. Inputs like ratings are also protected from value errors, accepting only floats
or integers.