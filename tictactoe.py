"""
x Create Board
x Logic to switch empty pieces with symbol
- compute moves to fill squares
x compute moves to check for winner
"""
import random

class T3Board:
    def __init__(self):
        self.board = [" "," "," "," "," "," "," "," "," "," "]
        self.fillCount = 0

    def checkForWin(self):
        if (self.board[0] == self.board[1] and self.board[0] == self.board[2]) and self.board[0] != " ":
            return True
        if self.board[3] == self.board[4] and self.board[3] == self.board[5] and self.board[3] != " ":
            return True
        if self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[6] != " ":
            return True
        if self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[0] != " ":
            return True
        if self.board[0] == self.board[3] and self.board[0] == self.board[6] and self.board[0] != " ":
            return True
        if self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] != " ":
            return True
        if self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != " ":
            return True
        if self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[2] != " ":
            return True
        return False

    def checkSimulation(self, computer):
        if (self.board[0] == self.board[1] and self.board[0] == self.board[2]):
            if self.board[0] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.board[3] == self.board[4] and self.board[3] == self.board[5]:
            if self.board[3] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.board[6] == self.board[7] and self.board[6] == self.board[8]:
            if self.board[6] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.board[0] == self.board[4] and self.board[0] == self.board[8]:
            if self.board[0] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.board[0] == self.board[3] and self.board[0] == self.board[6]:
            if self.board[0] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.board[1] == self.board[4] and self.board[1] == self.board[7]:
            if self.board[1] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.board[2] == self.board[5] and self.board[2] == self.board[8]:
            if self.board[2] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.board[2] == self.board[4] and self.board[2] == self.board[6]:
            if self.board[2] == computer:
                return "X"
            elif self.board[0] == "O":
                return "O"
        if self.fillCount == 9:
            return "tie"
        return None

    def drawSimulated(self):
        return self.fillCount == 9

    def isBoardFilled(self):
        return self.fillCount == 9

    def increaseFillCount(self, pos, symbol):
        if pos == -1:
            return
        self.board[pos] = symbol
        self.fillCount += 1

    def decreaseFillCount(self, pos):
        self.board[pos] = " "
        self.fillCount -= 1

    def cellEmpty(self, pos):
        return self.board[pos] == " "

    def returnEmptyPositions(self):
        pos = []
        for i in range(0, 9):
            if self.board[i] == " ":
                pos.append(i)
        if len(pos) == 0:
            return -1
        return pos


def getSymbol():
    player = input("Please select the symbol for Player 1. Enter 1 for X and 2 for O\n")
    while True:
        try:
            if int(player) < 1 or int(player) > 2:
                player = input("Invalid entry. Enter 1 for X and 2 for O\n")
            else:
                break
        except ValueError:
            print("Error: Value entered was not a number.\n")
            player = input("Enter a number in the correct range1 for X or 2 for O: ")

    if int(player) == 1:
        player = "X"
    else:
        player = "O"
    return player

def printBoard(board):
    count = 1
    line = ""
    for sp in board.board:
        if count % 3 == 0:
            line += sp
            print(line)
            line = ""
        else:
            line += sp + " | "
        count += 1

def validateMove(pos):
  temp = pos
  while True:
    try:
      if int(temp) > 9 or int(temp) < 1:
        temp = input("Enter a number in between 1-9 that hasn't been played yet: ")
      else:
        return int(temp)
    except ValueError:
      print("Error: Value entered was not a number.\n")
      temp = input("Enter a number in the correct range: ")


def checkGameStatus(player, board):
    if board.checkForWin():
        print(player + " has won the game!")
        exit()
    elif board.isBoardFilled():
        print("Game is a draw!")
        exit()

def runCompMove(computer, board):
    availablePos = board.returnEmptyPositions()
    bestScore = -100000000
    bestMove = -1
    for move in availablePos:
        board.increaseFillCount(move, computer)
        score = minimax(board, False)
        board.decreaseFillCount(move)
        if score >= bestScore:
            bestScore = score
            bestMove = move
    board.increaseFillCount(bestMove, computer)


def minimax(board, isMaximizing):
    score = board.checkSimulation("X")
    if score != None:
        return values[score]
    computer = "X"
    player = "O"
    emptyPos = board.returnEmptyPositions()
    if isMaximizing:
        bestScore = -10000000
        for move in emptyPos:
            board.increaseFillCount(move, computer)
            score = minimax(board, False)
            board.decreaseFillCount(move)
            if score > bestScore:
                bestScore = score
    else:
        bestScore = 10000000
        for move in emptyPos:
            board.increaseFillCount(move, player)
            score = minimax(board, True)
            board.decreaseFillCount(move)
            if score < bestScore:
                bestScore = score
    return bestScore

# def runCompMove(computer, board):
#     availablePos = board.returnEmptyPositions()
#     bestScore = -100000000
#     bestMove = -1
#     if availablePos == -1:
#         return
#     for move in availablePos:
#         board.increaseFillCount(move, computer)
#         score = minimax(board, True, computer)
#         board.decreaseFillCount(move)
#         if score == None:
#             continue
#         if score > bestScore:
#             bestScore = score
#             bestMove = move
#     print("Best score is " + str(score))
#     board.increaseFillCount(bestMove, computer)
#
# """
# Computer W : 1
# You W : -1
# Tie : 0
# """
#
# def minimax(board, isMaximizing, symbol):
#     score = board.checkSimulation(symbol)
#     if score == 0 or score == 1 or score == -1:
#         return score
#     if symbol == "X":
#         symbol = "O"
#     else:
#         symbol = "X"
#     emptyPos = board.returnEmptyPositions()
#     if emptyPos != -1:
#         emptyPos = []
#         if isMaximizing:
#             bestScore = -10000000
#             for move in emptyPos:
#                 board.increaseFillCount(move, symbol)
#                 score = minimax(board, False, symbol)
#                 board.decreaseFillCount(move)
#                 if score > bestScore:
#                     bestScore = score
#             print("Returning score is" + str(score) + " for " + symbol)
#             return bestScore
#         else:
#             bestScore = 10000000
#             for move in emptyPos:
#                 board.increaseFillCount(move, symbol)
#                 score = minimax(board, True, symbol)
#                 board.decreaseFillCount(move)
#                 if score < bestScore:
#                     bestScore = score
#             print("Returning score is" + str(score) + " for " + symbol)
#             return bestScore

values = {
    "X" : 10,
    "O" : -10,
    "tie": 0
}

def playVsComputer(board):
    player = "O"
    computer = "X"
    runCompMove(computer, board)
    printBoard(board)
    while not board.isBoardFilled():
        move = validateMove(input("Enter a location from 1 - 9: "))
        while True:
            if board.cellEmpty(move - 1):
                board.increaseFillCount(move - 1, player)
                break
            else:
                move = validateMove(input("Enter a location from 1 - 9. Previous location is occupied: "))
        checkGameStatus(player, board)
        runCompMove(computer, board)
        printBoard(board)
        checkGameStatus(player, board)

def playMultiPlayer(player, board):
    while not board.isBoardFilled():
        move = validateMove(input("Enter a location from 1 - 9: "))
        while True:
            if board.cellEmpty(move - 1):
                board.increaseFillCount(move - 1, player)
                break
            else:
                move = validateMove(input("Enter a location from 1 - 9. Previous location is occupied: "))
        printBoard(board)
        if checkGameStatus(player, board):
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

def mainMenu(board):
    option = input("Enter M for multiplayer mode,\nC for Computer\nor Q to quit.")
    while True:
        if option == "M":
            print("The pieces on the board have a number from 1 - 9, so level 1 has piece 1, 2, 3 and so on")
            player = getSymbol()
            playMultiPlayer(player, board)
        elif option == "C":
            print("You will play as O")
            print("The pieces on the board have a number from 1 - 9, so level 1 has piece 1, 2, 3 and so on")
            playVsComputer(board)
        elif option == "Q":
            exit()
        else:
            option = input("Invalid\nEnter M for multiplayer mode,\nC for Computer\nor Q to quit.")

print("Welcome to Shabir's TIc Tac Toe!")
board = T3Board()
print("Here is your board!")
printBoard(board)
mainMenu(board)