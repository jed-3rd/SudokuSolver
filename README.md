# SudokuSolver
A basic Sudoku game with built in auto-solver.

### About
The Sudoku Solver game uses an algorithm to develop new random Sudoku puzzles. Once the puzzle is generated it allows the user to use mouse and keyboard to enter digits to attempt to fill out the puzzle. Once the player wants to check the answers the player can click the "Check Answers" button. The program will then check all filled out answers and if it is correct it will lock in the answers and change the text color to green. If a player gives up the player can click the "Auto-Solve Puzzle" button, the program will then use a backtracking algorithm to solve the Sudoku puzzle in real time allowing the player to watch how the algorithm works. As the puzzle is being auto-solved the puzzle will be locked and the auto-solved squares will have red text. A player can get a new puzzle at any point by simply clicking the "New Puzzle" button.

### Dependancies
* Python 3.8.2
* PyQT5
