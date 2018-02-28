import sys

'''
    Elena Ryan | Quoridor Gameboard

    2.24.2018 v.1 -- Initial Functionality
        The class in its current state keeps track of both game pieces using position strings based on a 9x9 game board
        Walls are recorded using 64 bit binary numbers with 1 where a wall appears, the wh instance corresponds to horizontal strings, the wv corresponds to vertical
        Turn numbers are recorded both in wt and bt and keep track of game order and flow. t is only incremented after both wt and bt have been incremented
        Because neither player has unlimited walls, wb and ww keep track of the walls used, the limit being held in constant WALLS

        INIT
            bpos set to e9, the center of the bottom row; wpos set to e1, the center of the top row
            all turn variables initialized to 0
            number of walls used initialized to 0
            all possible wall positions initialized to 0

        updateBoard(self, turn, color, wall, pos)
            takes turn (int) and determines, based on turn and color (either 'b' or 'w'), whether it is the appropriate turn being played by the right player
            in the current iteration, if the play does not set a wall (denoted by 'v' or 'h'), and the pos is not occupied,
            and it is one away from cur pos, sets the color to that pos.

    
'''
class GameBoard:

    WALLS = 10      #Max available walls per player
    ROWS  = 9       #Rows
    COLS  = 9       #Columns

    def __init__(self):
        self.bpos = "e9" #initial black piece position
        self.wpos = "e1" #initial white piece position
        #finished = 0 #indicates if the game is finished
        self.t    = 0    # number of turns completed
        
        self.wt   = 0    #number of white turns completed
        self.bt   = 0    #number of black turns completed

        self.wb   = 0    #number of black walls used
        self.ww   = 0    #number of white walls used

        self.wh   =0b0000000000000000000000000000000000000000000000000000000000000000 # 64bit binary number representing horizontal walls
        self.wv   =0b0000000000000000000000000000000000000000000000000000000000000000 # 64bit binary number representing vertical walls

    def updateBoard(self, turn, color, wall, pos):
        #if it is a wall, v or h will be in the wall field, else it will = -1
        #must make sure no moves are happening out of turn using wt and bt counters, only incrementing turns after both have moved once
        print("Within updateBoard")

        # At some point, should determine what legal moves are, based on board size, piece position and walls
        if color == 'b' and turn == self.wt+1 :
            self.bt = self.bt+1
            if wall == -1:
                if pos != self.bpos and pos != self.wpos:  #actually need to make sure this is only being incremented by 1, see ASCII
                    self.bpos = pos
                else:
                    print("Cannot move the piece where there is already a piece")
            #handles moving the black piece
        if color == 'w' and turn == self.bt :
            self.wt = self.wt +1
            self.t = self.t+1
            if wall == -1:
                if pos != self.bpos and pos != self.wpos:
                    self.wpos = pos
                else:
                    print("Cannot move the piece where there is already a piece")
            #handles moving the white piece
            # no handling of walls yet

    def printBoard(self):
        #print("This is my HELL")
        #return 10
        print(self.bt)
        print("White piece is at "+str(self.wpos)+"\n")
        print("Black piece is at "+ str(self.bpos)+"\n")
        print("White has "+str(10-self.ww)+" walls remaining\n")        
        print("Black has "+str(10-self.wb)+" walls remaining\n")
        

        #include something here about the game being finished and who won
        
