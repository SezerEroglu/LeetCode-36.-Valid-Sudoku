# LeetCode-36.-Valid-Sudoku

For rows and columns, we create a list of allowed numbers from 1 to 9.
Then we check if the current element is "." or not. If not we check if the number is on the numbers list.
If it is we remove the number from the list and continue to the next element in row/column.
If it is not on the numbers list we return False.
After we check every row/column. We check every sub square.
We define ne middlepoints of every square then in 2d for loop raning from -1 to 1, we check every square in
similar fashion to the row/column check.
Finally we return True if not returned False before.

Runtime: Beats 60.76%
Memory: Beats 78.93%