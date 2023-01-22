from main import *



testTile = 1

#test cases 1, testing for method gameWinX


#Test case 1.1, 4 in a row horizontal
testBoard = copy.deepcopy(mainBoard)

testBoard[5][0] = testTile
testBoard[5][1] = testTile
testBoard[5][2] = testTile
testBoard[5][3] = testTile
if gameWinX(testBoard, testTile):
  print("Test 1.1 passed")
else:
  print("Test 1.1 failed")
print('\n')
#Test case 1.2, 4 in a row horizontal diff scenario
resetBoard(testBoard)
testBoard[5][0] = testTile
testBoard[5][1] = testTile
testBoard[5][2] = testTile
testBoard[4][6] = testTile
if not gameWinX(testBoard, testTile):
  print("Test 1.2 passed")
else:
  print("Test 1.2 failed")
print('\n')

print('\n')



#Test cases 2, testing for method gameWinY


#Test case 2.1, 4 in a row vertical diff scenario
resetBoard(testBoard)
testBoard[5][0] = testTile
testBoard[4][0] = testTile
testBoard[3][0] = testTile
testBoard[2][0] = testTile
if gameWinY(testBoard, testTile):
  print("Test 2.1 passed")
else:
  print("Test 2.1 failed")
print('\n')
#Test case 2.2, 4 in a row vertical different scenario
resetBoard(testBoard)
testBoard[5][0] = testTile
testBoard[0][1] = testTile
testBoard[1][1] = testTile
testBoard[2][1] = testTile
if not gameWinY(testBoard, testTile):
  print("Test 2.2 passed")
else:
  print("Test 2.2 failed")
print('\n')

print('\n')

  
# Test cases 3, Diagonal 4inArow method (gameWinSE)


# Test case 3.1, 4 in a row SE (should return win)
resetBoard(testBoard)

testBoard[0][0] = testTile
testBoard[1][1] = testTile
testBoard[2][2] = testTile
testBoard[3][3] = testTile
printBoard(testBoard)
if gameWinSE(testBoard, testTile):
  print("Test 3.1 passed")
else:
  print("Test 3.1 failed")
print('\n')
# Test case 3.2, 4 in a row SE (should not return win)
resetBoard(testBoard)

testBoard[3][0] = testTile
testBoard[2][3] = testTile
testBoard[1][2] = testTile
testBoard[0][3] = testTile
printBoard(testBoard)
if not gameWinSE(testBoard, testTile):
  print("Test 3.2 passed")
else:
  print("Test 3.2 failed")
print('\n')
# Test case 3.3, 4 in a row SE (should not return win)
resetBoard(testBoard)

testBoard[2][6] = testTile
testBoard[3][5] = testTile
testBoard[4][4] = testTile
testBoard[5][3] = testTile
printBoard(testBoard)
if not gameWinSE(testBoard, testTile):
  print("Test 3.3 passed")
else:
  print("Test 3.3 failed")
print('\n')


print('\n')
  
  
# Test cases 4, Diagonal 4inArow method (gameWinNE)


# Test case 4.1, 4 in a row NE (should return win)
resetBoard(testBoard)

testBoard[0][3] = testTile
testBoard[1][2] = testTile
testBoard[2][1] = testTile
testBoard[3][0] = testTile
printBoard(testBoard)
if gameWinNE(testBoard, testTile):
  print("Test 4.1 passed")
else:
  print("Test 4.1 failed")
print('\n')
# Test case 4.2, 4 in a row NE (should not return win)
resetBoard(testBoard)

testBoard[3][0] = testTile
testBoard[2][3] = testTile
testBoard[1][2] = testTile
testBoard[0][3] = testTile
printBoard(testBoard)
if not gameWinNE(testBoard, testTile):
  print("Test 4.2 passed")
else:
  print("Test 4.2 failed")
print('\n')
# Test case 4.3, 4 in a row NE (should return win)
resetBoard(testBoard)

testBoard[2][6] = testTile
testBoard[3][5] = testTile
testBoard[4][4] = testTile
testBoard[5][3] = testTile
printBoard(testBoard)
if gameWinNE(testBoard, testTile):
  print("Test 4.3 passed")
else:
  print("Test 4.3 failed")
print('\n')

print('\n')


#Test cases 5.1

#Test case 5.1, tilecounters Testing
resetBoard(testBoard)
testBoard[5][0] = testTile
testBoard[5][1] = testTile
testBoard[5][2] = testTile
testBoard[5][3] = testTile
testBoard[0][3] = testTile
testBoard[0][4] = testTile
testBoard[0][5] = testTile
testBoard[0][6] = testTile
testBoard[4][3] = testTile
testBoard[4][4] = testTile
testBoard[4][5] = testTile
testBoard[4][6] = testTile
printBoard(testBoard)
if tileCounterX(testBoard, testTile, 3) == 3:
  print("Test 5.1 passed")
else:
  print("Test 5.1 failed")
  
