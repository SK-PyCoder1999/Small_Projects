board = [' ' for i in range(10)]  # we will not use index 0 .
#print(board)

def insertLetter(letter,posi):
    board[posi]=letter
        
def printBoard(board):
    print("   |   |   ")
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("   |   |   ")
#DummyBoard=[' ','1','2','3','4','5','6','7','8','9']    
#printBoard(DummyBoard)

def isSpaceFree(posi):
    TorF = (board[posi] == ' ')
    return TorF    
def isBoardFull(board):
    if board.count(' ') > 1 :   # because board[0] always have ' ' .
        return False
    else:
        return True        
#DummyBoard=[' ','1','2','3','4','5','6','7','8','9']    
#print(isBoardFull(DummyBoard))

def isWinner(board,letter):
    b=board
    l=letter
    TorF = ( ( b[1]==l and b[2]==l and b[3]==l ) or
    ( b[4]==l and b[5]==l and b[6]==l ) or
    ( b[7]==l and b[8]==l and b[9]==l ) or  # Done for all three rows
    ( b[1]==l and b[4]==l and b[7]==l ) or
    ( b[2]==l and b[5]==l and b[8]==l ) or
    ( b[3]==l and b[6]==l and b[9]==l ) or  # Done for all three columns
    ( b[1]==l and b[5]==l and b[9]==l ) or
    ( b[3]==l and b[5]==l and b[7]==l ) )   # Done for both diagonal
    return TorF
#DummyBoard=[' ','1','1','1','4','5','6','7','8','9']    
#print(isWinner(DummyBoard,'1'))

def playerMove():
    run=True
    while run :
        move=input("Please select a position to enter the 'X' between 1 to 9 (inclusive) on the Board : ")
        try:
            move=int(move)
            if move>0 and move<10 :
                if isSpaceFree(move) :
                    insertLetter('X',move)
                    run=False
                else:
                    print("Sorry, this place is occupied.")
            else:
                print("Please type a number between 1 to 9 only.")
        except:
            print("Please type only a number")

def computerMove():
    #possible_moves=[]
    #for v,letter in enumerate(board):
    #    if board[v]==' ' and v!=0 :     # Because we will not use 0 index anywhere.
    #        possible_moves.append(v)
    #OR we can write above 4-lines code in one line as bellow...
    possible_moves = [ v for v,letter in enumerate(board) if board[v]==' ' and v!=0 ]  
    #We will take bydefault move as 0 (which is not possible basically).
    move=0
    #check that computer's win confirm or spoil the player's win 
    for let in ['O','X']:
        for i in possible_moves:
            board_copy=board[:]
            board_copy[i]=let
            if isWinner(board_copy,let):
                move=i
                return move
    #Now for the winning purpose computer will target corner's values(1,3,7,9)[first priority], 
    #then mid value(5) And then edge's values(2,4,6,8)
    posi_corner_moves=[]
    for i in possible_moves:
        if i in [1,3,7,9]:
            posi_corner_moves.append(i)
    if len(posi_corner_moves) > 0 :
        move=selectRandom(posi_corner_moves) #We will also define this Fn. after ending of computerMove() Fn.
        return move
    
    if 5 in possible_moves:
        move=5
        return move
        
    posi_edge_moves=[]
    for i in possible_moves:
        if i in [2,4,6,8]:
            posi_edge_moves.append(i)
    if len(posi_edge_moves) > 0 :
        move=selectRandom(posi_edge_moves) #We will also define this Fn. after ending of computerMove() Fn.
        return move
    
    #Below line is the most imported line Because if you forget it,
    #there will be a error occur in full-Board case (inaprropriate value of move). 
    return move    #It will work only in case when move==0 . 
        
def selectRandom(lst):
    import random
    ln=len(lst)
    r=random.randrange(0,ln) #Will find the random index value
    return lst[r]

def mainLogic():
    print("Welcome to the game")
    printBoard(board)
    
    while not(isBoardFull(board)):
        #Player's movement
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, you loose the game !")
            break    
        #Computer's movement
        if not(isWinner(board,'X')):
            move=computerMove()
            if move==0 :
                print(" ")  #Will run only when board will full
            else:
                insertLetter('O',move)
                print("Computer placed an 'O' on position",move,":")
                printBoard(board)
        else:
            print("Congratulations, you win the game !! ")
            break
            
    if isBoardFull(board):
        print("TIE GAME")

#Interface of Game .....
print("Tic-Tac-Toe Game")
x=input("Do you want to play this game, Please press 'y' for yes And 'n' for no : ")
while True:
    if x.lower() == 'y' :
        board = [' ' for i in range(10)]    # Here initialising board is also essential
        print("*****************************")
        mainLogic()
    else:
        break 
    x=input("Do you want to play again ? (y/n) : ")