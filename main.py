#Header:  
#Name: Jawad Abdel Mouhsen 
#Date:  January 20, 2023
#Class: ICS3U
#Teacher: Mr.Tombs
#Program Name: Connect-4-Game 
#Purpose: Conncet-4-game, that is able to be played in multiple modes such as: PVP and AI. As well as hold other features such as a leaderboard. 

#libraries setup
from numpy import square
import pygame
import sys
from datetime import datetime
import math
import random
import time
from time import sleep
import copy
#Setup Board

#Colours Inventory: 
blue =  (3, 155, 229) #(Colour for Board)
black = (0,0,0) #(Black for background)
red = (255,0,0) #(For red tile)
white = (255,255,255) #(For leaderboard colour)
yellow = (255,255,0) #(for yellow tile)
green = (57,255,20) 
color_light = (165,50,47)

pygame.init()


mainBoard = [ #Making the array for the gameboard that will hold the tiles
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0]
]

def resetBoard(board): #useful method for testing etc. clears up the board. Resets board row counter to 0. 
  for row in range(6):
    for col in range(7):
      board[row][col] = 0

#Helper methods

def printBoard(board): #Drawing the board on console
  print("   1   2   3   4   5   6   7")
  
  for row in range(6):
    print(" |---+---+---+---+---+---+---|")
    print(" | ", end = '')
    
    for col in range(7):
      if board[row][col] == 0:
        print( ' ' + " | ", end = '')
      else:
        print( str(board[row][col]) + " | ", end = '')
    print("")
  print(" |---+---+---+---+---+---+---|")
  print('')

#It goes through the rows of the board starting from the bottom most row and checks if the current position is empty. If it is, the piece
#is placed there, otherwise the loop continues until an empty spot is found. If not an Error is printed. 
def placeTile(currentBoard, col, piece):  #Method for Placing Tile in Board
  y=5
  for row in range(6):
    # if currentBoard[0][col] != 0:
    #   print("Column is full.\n")
    #   break
    
    if currentBoard[y][col] == 0:
      currentBoard[y][col] = piece
      break
    elif currentBoard[y][col] != 0:
      y-=1
      
    else: #Dummy Proofing
      print("Error.")
      break

def removeTile(currentBoard, col, piece):  #Method for Removing Tile in Board
  y=0
  for i in range(6):
    if currentBoard[y][col] == piece:
      currentBoard[y][col] = 0
      break

    elif currentBoard[y][col] == 0:
      y+=1
    else:
      break

def allowedMove(currentBoard, col): #Checks if move is legal (wont give an error) (PvP)
  continues = True
  
  if choice >= 7 or choice <0:
    # print("\nColumn does not Exist. Try Again.\n")
    continues = False
    return continues
    
  elif currentBoard[0][col] != 0:
    # print("\nColumn is full. Try Again.\n")
    continues = False
    return continues
    
  return continues

#The function "getAllowedMoves" takes in a board and returns a list of all columns where legal moves can be made.
#It calls the "allowedMove" function for each column and adds the column to the list if the function returns True.
def getAllowedMoves(board): #Returns list with available moves (AI)
  moves = []
  for i in range(7):
    if allowedMove(board, i):
      moves.append(i)
  return moves

def gameWinX(Board, tile): #Count 4 in a row X. Checking the the ranges of the board. When Counter=4 the loop breaks, returning a Win.  
  counter = 0
  win = False
  for row in range(6):
    for col in range(7):
      if Board[row][col] == tile:
        counter +=1
      else:
        counter = 0
      if counter == 4:
        win = True
        break
    counter = 0
  return win

#Count 4 in a row Y. Checking the the ranges of the board. When Counter=4 the loop breaks, returning a Win.  
def gameWinY(Board, tile):
  counter = 0
  win = False
  for col in range(7):
    for row in range(6):
      if Board[row][col] == tile:
        counter +=1
      else:
        counter = 0
      if counter == 4:
        win = True
        break
    counter = 0
  return win

def gameWinNE(Board, tile): #Count 4 in a row Diagonal NE. Checking the the ranges of the board. When Counter=4 the loop breaks, returning a Win.  
  counter = 0
  win = False
  for x in range(12):
    if x<=5:
      for i in range(x,-1,-1):
        if Board[i][x-i] == tile:
          counter +=1
        else:
          counter = 0
        if counter == 4:
          win = True
          return win

    else:
      for i in range(5,x-7,-1):
        if Board[i][x-i] == tile:
          counter +=1
        else:
          counter = 0
        if counter == 4:
          win = True
          return win
        
    counter = 0
  return win

def gameWinSE(Board, tile): #Count 4 in a row Diagonal SE. Checking the the ranges of the board. When Counter=4 the loop breaks, returning a Win.  
  counter = 0
  win = False
  
  for x in range(12):
    if x<=5:
      for i in range(x,-1,-1):
        if Board[5-i][x-i] == tile:
          counter += 1
        else:
          counter = 0
        if counter == 4:
          win = True
          return win
      
    else:
      for i in range(5,x-7,-1):
        if Board[5-i][x-i] == tile:
          counter += 1
        else:
          counter = 0
        if counter == 4:
          win = True
          return win

    counter = 0      
      
  return win
#Uses the counting 4inarow methods in one method
#Main method. Recongizes the win. 
def winningBoard(Board, tile):
  win = False
  if gameWinX(Board, tile) or gameWinY(Board, tile) or gameWinNE(Board, tile) or gameWinSE(Board, tile):
    win = True
    return win


  
#AI Methods


#Tilecounter helper methods
def tileCounterX(Board, tile, count): # Loop Counts tiles in a row Horizontally
  counter = 0
  counts = 0
  for row in range(6):
    for col in range(7):
      if Board[row][col] == tile:
        counter +=1
      else:
        counter = 0
      
      if counter == count:
        counts += 1
        counter = 0
  
    counter = 0
  return counts

def tileCounterY(Board, tile, count): #loop Counts tiles in a row Vertically
  counter = 0
  counts = 0
  for col in range(7):
    for row in range(6):
      if Board[row][col] == tile:
        counter +=1
      else:
        counter = 0
      if counter == count:
        counts += 1
        counter = 0
        
    counter = 0
  return counts

def tileCounterNE(Board, tile, count): #loop Counts tiles in a row Diagonal NE
  counter = 0
  counts = 0
  for x in range(12):
    if x<=5:
      for i in range(x,-1,-1):
        if Board[i][x-i] == tile:
          counter +=1
        else:
          counter = 0
          
        if counter == count:
          counts += 1

    else:
      for i in range(5,x-7,-1):
        if Board[i][x-i] == tile:
          counter +=1
        else:
          counter = 0
        if counter == count:
          counts += 1

        
    counter = 0
  return counts

def tileCounterSE(Board, tile, count): #loop Count 4 in a row Diagonal SE
  counter = 0
  counts = 0
  
  for x in range(12) :
    if x<=5:
      for i in range(x,-1,-1):
        if Board[5-i][x-i] == tile:
          counter += 1
        else:
          counter = 0
        if counter == count:
          counts+=1
      
    else:
      for i in range(5,x-7,-1):
        if Board[5-i][x-i] == tile:
          counter += 1
        else:
          counter = 0
        if counter == count:
          counts+=1

    counter = 0      
      
  return counts

#Tilecounter main method
def tileCounter(Board, tile, count): #tileCounter counts the amount of tiles in a row given amount
  points = 0
#The tileCounter main method calls each of the functions and adds the results to a variable "points". It then returns the total points.
  points += tileCounterX(Board, tile, count)
  points += tileCounterY(Board, tile, count)
  points += tileCounterNE(Board, tile, count)
  points += tileCounterSE(Board, tile, count)

  return points

def getVal(board, move, tile): #getValue does the move and returns value of the move 
  newBoard = copy.deepcopy(board)
  value = 0
  placeTile(newBoard, move, tile)
  
  if winningBoard(newBoard, tile):
    value+=1000000

  value += tileCounter(newBoard, tile, 2) * 2
  value += tileCounter(newBoard, tile, 3) * 6

  #if placed in the middle column
  if move == 3:
    value += 10


    
  return value
#The function checks if the game is over by calling the winningBoard function to check if the AI or player has won or if the list of allowed moves is empty.
def isGameOver(board): #board states when game is over. for the minimax algortithm #
  return winningBoard(board, AITile) or winningBoard(board, pTile) or len(getAllowedMoves(board)) == 0

def boardVal(board, tile): #function for only checking the value of the board (for minmax)
  value = 0
  if winningBoard(board, tile):
    value+=1000000
  value += tileCounter(board, tile, 2) * 3
  value += tileCounter(board, tile, 3) * 7
  for row in range(6):
    if board[row][4] == tile:
      value+=15
      break
   
  return value
#Minimax Alorgithim is a decision-making algorithm that is used in two-player games, to get the best decision for an AI machine.
#Minimax was learned and used from: https://www.youtube.com/watch?v=MMLtza3CZFM
def minimax(board, depth, alpha, beta, maximizingPlayer): #MinMax Algorithm. 
  validLocations = getAllowedMoves(board)
  gameOver = isGameOver(board) #First thing checks if the game is over. 
  if depth == 0 or gameOver: 
    if gameOver:
      if winningBoard(board, AITile): #If statement for game is over. Gives the AI a value of 100000000.
        return (None, 100000000)
      elif winningBoard(board, pTile): #If player won. Gives a -100000000 value. 
        return (None, -100000000)
      else:
        return (None, 0) #If the game is a tie returns a value of 0. 
    else:
      return (None, boardVal(board, AITile))

  if maximizingPlayer: #AIs turn (maximizing)
    val = -math.inf
    col = random.choice(validLocations)

    for i in validLocations:
      newBoard = copy.deepcopy(board)
      placeTile(newBoard, i, AITile)
      newVal = minimax(newBoard, depth-1, alpha, beta, False)[1]
      if newVal > val:
        val = newVal
        col = i
      alpha = max(alpha, val) #alpha beta pruning (The alpha-beta pruning is used to cut off things that will not be chosen in the final decision, therefore reducing the time complexity of the algorithm.)
      if alpha >= beta:
        break
    return col, val


  
  else:   #Players turn (minimizing)
    val = math.inf
    col = random.choice(validLocations)

    for i in validLocations:
      newBoard = copy.deepcopy(board)
      placeTile(newBoard, i, pTile)
      newVal = minimax(newBoard, depth-1, alpha, beta, True)[1]
      if newVal < val:
        val = newVal
        col = i
      beta = min(beta, val)
      if alpha >= beta:
        break
        
    return col, val

    
#Pygame methods
def drawBoard(board): #Draws the board in pygame
  for c in range(7):
    for r in range(6):
      pygame.draw.rect(screen, blue, (c*squaresize, r*squaresize+squaresize, squaresize, squaresize))
      pygame.draw.circle(screen, black, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), radius)

  for c in range(7):
    for r in range(6):		
      if board[r][c] == 1:
        pygame.draw.circle(screen, red, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), radius)
      elif board[r][c] == 2: 
        pygame.draw.circle(screen, yellow, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), radius)
  pygame.display.update()


def getLeaderboard(): #this prints the content of the leaderboard.txt file
  boardfile = open('leaderboard.txt')
  boardlist = []
  print('\n\n')
  for line in boardfile.readlines():
    boardlist.append(line)
  return boardlist

#Text formating 
def draw_text(text, font, color, surface, x, y):
  textobj = font.render(text, 1, color)
  textrect = textobj.get_rect()
  textrect.topleft = (x, y)
  surface.blit(textobj, textrect)




#Actual Game 
currentBoard = mainBoard


#For Formatting 
squaresize = 100
width = 7 * squaresize
height =  (6+1) * squaresize
size = (width, height)
radius = int(squaresize/2 - 5)
myfont = pygame.font.SysFont('monospace', 75)
myfont2 = pygame.font.SysFont('monospace', 15)
myfont3 = pygame.font.SysFont('monospace', 45)
myfont4 = pygame.font.SysFont('monospace', 19, bold=True)

exitBox1 = pygame.Rect(15, 585, 90,90)


screen = pygame.display.set_mode(size)
pygame.display.update()
    
def leaderboardAdd(timetaken):
  date = str(datetime.today().strftime('%Y-%m-%d'))
  scoreFile = open('leaderboard.txt', 'a')
  scoreFile.write('Date: '+date+',  Time taken: '+str(timetaken)+'s\n')

def winBoard(leaderboard):
  winning = True


  while winning:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()



      screen.fill("white")
      draw_text("Leaderboard:", myfont3, black, screen, 17, 10)
      
      exit1 = pygame.image.load("/Users/Desktop/Final Project/Workspace/pics/exit.png").convert_alpha()
      exit1 = pygame.transform.scale(exit1, (100, 100))
      pygame.draw.rect(screen, white, exitBox1)
      screen.blit(exit1, (10,580))

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button.
          # Check if the rect collides with the mouse pos.
          if exitBox1.collidepoint(event.pos):
            sys.exit()
      x=60
      for i in leaderboard:
        draw_text(str(i), myfont2, black, screen, 20, x)
        x+=30
      pygame.display.update()

#Main Menu Buttons
mainMenu = True
pvpBox = pygame.Rect(195, 150, 320, 105)
aiBox = pygame.Rect(195, 320, 320, 105)
boardBox = pygame.Rect(275, 490, 150, 60)
exitBox = pygame.Rect(30, 600, 60,60)

#For Quiting the Game
while mainMenu:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    screen.fill("black")
#Images gathered from the internet and uploaded to Computer. 
    imp1 = pygame.image.load("/Users/Desktop/Final Project/Workspace/pics/back.png").convert()
    button1 = pygame.image.load('/Users/Desktop/Final Project/Workspace/pics/button1.png').convert_alpha()
    button1 = pygame.transform.scale(button1, (375, 150))
    button2 = pygame.image.load('/Users/Desktop/Final Project/Workspace/pics/button1.png').convert_alpha()
    button2 = pygame.transform.scale(button2, (375, 150))
    button3 = pygame.image.load('/Users/Desktop/Final Project/Workspace/pics/button1.png').convert_alpha()
    button3 = pygame.transform.scale(button3, (375, 150))
    exit1 = pygame.image.load("/Users/Desktop/Final Project/Workspace/pics/exit.png").convert_alpha()
    exit1 = pygame.transform.scale(exit1, (100, 100))
    
    # Using blit to copy content from one surface to other
    screen.blit(imp1, (0, 0))
    
    draw_text("Welcome to connect four!", myfont4, white, screen, 20, 50)
    draw_text("Please select the GameMode you would like to play.", myfont4, white, screen, 20, 80)
    
    pygame.draw.rect(screen, color_light, pvpBox)
    screen.blit(button1, (165, 130))
    draw_text("PvP", myfont, white, screen, 290, 165)

    pygame.draw.rect(screen, color_light, aiBox)
    screen.blit(button2, (165, 300))
    draw_text("AI", myfont, white, screen, 310, 335)

    pygame.draw.rect(screen, color_light, boardBox)
    screen.blit(button3, (165, 470))
    draw_text("Board", myfont, white, screen, 245, 505)

    pygame.draw.rect(screen, color_light, exitBox)
    screen.blit(exit1, (10,580))

    pygame.display.update()
    # mx, my = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:  # Left mouse button.
        # Check if the rect collides with the mouse pos.
        if pvpBox.collidepoint(event.pos):
          gameMode = "P"
          mainMenu = False
        elif aiBox.collidepoint(event.pos):
          gameMode = "AI"
          mainMenu = False
        elif boardBox.collidepoint(event.pos):
          gameMode = "BOARD"
          mainMenu = False
        elif exitBox.collidepoint(event.pos):
          sys.exit()


drawBoard(currentBoard)
pygame.display.update()

if gameMode == "BOARD": #Shows scores of all players
  winBoard(getLeaderboard())

elif gameMode == "P":
  #Setup Game
  pTile = 1
  p2Tile = 2
  turn = 1

  #Game Start
  game = True
  print('\n')
  start = time.time()
  printBoard(currentBoard)
  
  while game:
    #pygame setup
    for event in pygame.event.get():
      if event.type == pygame.QUIT: #makes the game end when you exit the tab
        sys.exit()

      if event.type == pygame.MOUSEMOTION:
        pygame.draw.rect(screen, black, (0,0, width, squaresize))
        xpos = event.pos[0]
        if turn == 1:
          pygame.draw.circle(screen, red, (xpos, int(squaresize/2)), radius)
        else: 
          pygame.draw.circle(screen, yellow, (xpos, int(squaresize/2)), radius)
      pygame.display.update()

      if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.rect(screen, black, (0,0, width, squaresize))

        #Player 1
        if turn == 1:
          print("\n\nPlayer 1's turn.\n")
          
          
          xpos = event.pos[0]
          choice = int(math.floor(xpos/squaresize))
          printBoard(currentBoard)
            
          print('')
          if allowedMove(currentBoard, choice): 
            placeTile(currentBoard, choice, pTile)
            turn +=1
          printBoard(currentBoard)
          drawBoard(currentBoard)
          
          #Checks if game over
          if winningBoard(currentBoard, pTile):
            screen.fill("black")
            win1 = pygame.image.load("/Users/Desktop/Final Project/Workspace/pics/win.png").convert_alpha()
            screen.blit(win1, (0, 0))
            draw_text("Player 1 wins!!", myfont, red, screen, 10, 10)
            pygame.display.update()
            print('')
            
            print("\n\nGame Over. Player 1 Wins!!\n")
            printBoard(currentBoard)

            pygame.time.wait(10000)
            game = False

          elif len(getAllowedMoves(currentBoard)) == 0: #Check if board is full (Tie). It does that by checking the "getAllowedMoves" when moves equals 0 prints a Tie. 
            print('')
            printBoard(currentBoard)
            pygame.time.wait(3000)
            print("\n\nGame Over. Board is Full & it's a TIE!!\n")
            printBoard(currentBoard)
            game = False

            
        # #Player 2
        elif turn == 2:
          print("\n\nPlayer 2's turn.\n")
          
          
          xpos = event.pos[0]
          choice = int(math.floor(xpos/squaresize))
          printBoard(currentBoard)
            
          print('')
          if allowedMove(currentBoard, choice):
            placeTile(currentBoard, choice, p2Tile)
            turn -=1
          printBoard(currentBoard)
          drawBoard(currentBoard)
          
          #Checks if game over
          if winningBoard(currentBoard, p2Tile):
            screen.fill("black")
            win1 = pygame.image.load("/Users/anas/Desktop/Final Project/Workspace/pics/win.png").convert_alpha()
            screen.blit(win1, (0, 0))
            draw_text("Player 2 wins!!", myfont, yellow, screen, 10, 10)
            pygame.display.update()
            print('')
            
            print("\n\nGame Over. Player 2 Wins!!\n")
            printBoard(currentBoard)

            pygame.time.wait(10000)
            game = False

          elif len(getAllowedMoves(currentBoard)) == 0:
            print('')
            printBoard(currentBoard)
            pygame.time.wait(10000)
            print("\n\nGame Over. Board is Full & it's a TIE!!\n")
            printBoard(currentBoard)
            game = False

  
  
elif gameMode == "AI":
  #Setup Game
  pTile = 1
  AITile = 2
  turn = 1

  #Game Start
  game = True
  start = time.time()
  print('\n')

  while game:
    #pygame setup
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEMOTION:
        pygame.draw.rect(screen, black, (0,0, width, squaresize))
        xpos = event.pos[0]
        if turn == 1:
          pygame.draw.circle(screen, red, (xpos, int(squaresize/2)), radius)
        else: 
          pass
      pygame.display.update()

      if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.rect(screen, black, (0,0, width, squaresize))

        #Players turn 
        if turn == 1:
          print("\n\nPlayer 1's turn.\n")
          
          
          xpos = event.pos[0]
          choice = int(math.floor(xpos/squaresize))
          printBoard(currentBoard)

          a = random.randint(1,2)
          if a == 2:
            randfile = open('random.txt')
            listFile = []
            for line in randfile.readlines():
              listFile.append(line)
            print(random.choice(listFile))
            print('\n')

            
          print('')
          if allowedMove(currentBoard, choice):
            placeTile(currentBoard, choice, pTile)
            turn +=1
          printBoard(currentBoard)
          drawBoard(currentBoard)
          
          #Checks if game over
          if winningBoard(currentBoard, pTile):
            print('')
            printBoard(currentBoard)
            print("\n\nGame Over. Player 1 Wins!!\n")

            screen.fill("black")
            imp2 = pygame.image.load("/Users/Desktop/Final Project/Workspace/pics/win.png").convert_alpha()
            screen.blit(imp2, (0, 0))
            draw_text("Player 1 wins!!", myfont, red, screen, 10, 10)
            pygame.display.update()
            timetaken = round((time.time() - start), 2)
            
            leaderboardAdd(timetaken)
            pygame.time.wait(10000)
            winBoard(getLeaderboard())
            pygame.display.update()
            pygame.time.wait(15000)
            game = False
          #Checks if board is full
          elif len(getAllowedMoves(currentBoard)) == 0:
            print('')
            printBoard(currentBoard)
            print("\n\nGame Over. Board is Full & it's a TIE!!\n")
            printBoard(currentBoard)
            pygame.time.wait(10000)
            game = False


    #AIs Turn
    if turn == 2 and game:
      print("\n\nAI's turn.\n")
      printBoard(currentBoard)

      choice = 0

      choice, score = minimax(currentBoard, 7, -math.inf, math.inf, True)

      print("\n")
      print("AI chose column " + str(choice+1))
        
      placeTile(currentBoard, choice, AITile)
      drawBoard(currentBoard)

      #Checks if game over
      if winningBoard(currentBoard, AITile):
        screen.fill("black")
        lose = pygame.image.load("/Users/Desktop/Final Project/Workspace/pics/lose.png").convert_alpha()
        screen.blit(lose, (0, 0))
        draw_text("AI wins!!", myfont, blue, screen, 150, 10)
        pygame.display.update()
        print('')
        printBoard(currentBoard)
        
        print("\n\nGame Over. AI Wins!!\n")
        printBoard(currentBoard)

        pygame.time.wait(10000)
        game = False
      elif len(getAllowedMoves(currentBoard)) == 0:
        print('')
        printBoard(currentBoard)
        print("\n\nGame Over. Board is Full & it's a TIE!!\n")
        printBoard(currentBoard)
        pygame.time.wait(10000)
        game = False
  
      turn-=1

else:
  print("Run program again and select an actual mode ")
