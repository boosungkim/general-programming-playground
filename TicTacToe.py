#The Board
TTT = {"top-L": " ", "top-M": " ", "top-R": " ", "mid-L": " ", "mid-M": " ", "mid-R": " ", "low-L": " ", "low-M": " ", "low-R": " "}
def printB(board):
    print(board["top-L"] + " |" + board["top-M"] + " |" + board["top-R"])
    print("--+--+--")
    print(board["mid-L"] + " |" + board["mid-M"] + " |" + board["mid-R"])
    print("--+--+--")
    print(board["low-L"] + " |" + board["low-M"] + " |" + board["low-R"])

print("Positions are top-L, top-M, top-R, and there are top, mid, and low.")

turn = "X"
for i in range(9):
    printB(TTT)
    print("Turn for " + turn + ". Move to which place?")
    move = input()
    TTT[move] = turn

    if turn == "X":
        turn = "O"
    else:
        turn = "X"


