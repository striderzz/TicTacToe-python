myboard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1 = 0
player2 = 0
gameOver = False


def displayBoard():
    print("\n")
    print(myboard[0], "|" + myboard[1], "|" + myboard[2])
    print("---------")
    print(myboard[3], "|" + myboard[4], "|" + myboard[5])
    print("---------")
    print(myboard[6], "|" + myboard[7], "|" + myboard[8])


def placeMarker(position, playerTurn):
    myboard[position] = playerTurn
    displayBoard()


def CheckPosition(position):
    if position > 8:
        print("Enter a valid position between 0 - 8")
        return
    if myboard[position] == "X" or myboard[position] == "O":
        print("Position is occupied, choose another position!")
    else:
        return True


def CheckForWin():
    global gameOver

    if (myboard[0] == myboard[1] == myboard[2] == "X" or
            myboard[3] == myboard[4] == myboard[5] == "X" or
            myboard[6] == myboard[7] == myboard[8] == "X" or
            myboard[0] == myboard[3] == myboard[6] == "X" or
            myboard[1] == myboard[4] == myboard[7] == "X" or
            myboard[2] == myboard[5] == myboard[8] == "X" or
            myboard[0] == myboard[4] == myboard[8] == "X" or
            myboard[2] == myboard[4] == myboard[6] == "X"

    ):

        print("\nX Wins!")
        gameOver = True
    elif (myboard[0] == myboard[1] == myboard[2] == "O" or
          myboard[3] == myboard[4] == myboard[5] == "O" or
          myboard[6] == myboard[7] == myboard[8] == "O" or
          myboard[0] == myboard[3] == myboard[6] == "O" or
          myboard[1] == myboard[4] == myboard[7] == "O" or
          myboard[2] == myboard[5] == myboard[8] == "O" or
          myboard[0] == myboard[4] == myboard[8] == "O" or
          myboard[2] == myboard[4] == myboard[6] == "O"):
        print("\nO Wins!")
        gameOver = True

    if " " not in myboard:
        print("\nDraw! ")
        gameOver = True


def StartGame():
    moveCount = 0
    markerType = input("choose X or 0:(X/0)\n")
    if markerType.lower() == "x":
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"

    displayBoard()
    while gameOver == False:
        position = int(input("Enter position: "))
        if (moveCount % 2 == 0):
            if (CheckPosition(position)):
                placeMarker(position, player1)
                moveCount += 1
                CheckForWin()
        else:
            if (CheckPosition(position)):
                placeMarker(position, player2)
                moveCount += 1
                CheckForWin()


while gameOver == False:
    playgame = input("Do you want play Tic Tac Toe?(Y/N):\n")
    if (playgame.lower() == "n"):
        quit()
    elif playgame.lower() == "y":
        StartGame()