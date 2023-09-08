from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] not in numbers:
                        return False
                    numbers.remove(board[i][j])
        for i in range(0, 9):
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
            for j in range(0, 9):
                if board[j][i] != ".":
                    if board[j][i] not in numbers:
                        return False
                    numbers.remove(board[j][i])
        middlePoints = []
        for i in range(0, 3):
            for j in range(0, 3):
                middlePoints.append([1 + i * 3, 1 + j * 3])

        for pos in middlePoints:
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if board[pos[0] + j][pos[1] + i] != ".":
                        if board[pos[0] + j][pos[1] + i] not in numbers:
                            return False
                        numbers.remove(board[pos[0] + j][pos[1] + i])

        return True
