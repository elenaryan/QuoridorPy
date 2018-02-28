
import sys
from QuorBoard import GameBoard

'''
    Quoridor driver.  Takes as input a file of (HOPEFULLY) valid quoridor moves
    splices them into moves and then updates the game board.  At present we're working
    pulling the moves into something the updateFunction will understand and be able to
    check and implement.

'''
def parseMove(mLine):
    mLine = mLine.split(";")#splits each turn into its two moves
    return mLine





if __name__ == '__main__':
    f = raw_input("Enter a file containing quoridor moves.  The appropriate format is <turn number><color>.<column><row><OPTIONALdirection>\ni.e. 1b.e8 means on the first round black moves to the 8th position.\n")
    gb = GameBoard()
    fp = open(f, 'r')
    for line in fp.readline():
        b = parseMove(line);
        #update gameboard
        for move in b:
            #we can just check length to determine whether wall or not
            if len(move) != 6:
                gb.updateBoard(int(move[0]), move[1], -1, move[3:])
            else:
                gb.updateBoard(int(move[0]), move[1], move[5], move[3:4])
                
    gb.updateBoard(1, "b", -1, "e8")
    gb.printBoard()
