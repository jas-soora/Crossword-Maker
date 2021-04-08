#Jastejpal Soora

blank = ' '
board = [[blank]*20 for i in range(20)]

def printboard(board): #function to create the grid for the crossword
    bL = len(board)

    print(' '+'_'*bL)

    for i in range(bL):
        print('|', end='')

        for j in range(bL):
            print(board[i][j], end='')
        print('|')

    print(' '+'-'*bL)

def verticalCheck(board, word, position, row, col): #function to check if a word can be placed vertically legally
    firstpos = row-position

    if board[row-1][col-1] != blank or board[row-1][col+1] != blank: #ensures that board does not create illegal adjacencies
        return False

    if board[row+1][col-1] != blank or board[row+1][col+1] != blank: #ensures that board does not create illegal adjacencies
        return False

    elif board[row-1][col] != blank or board[row+1][col] != blank: #ensures that word does not overwrite words on board, print reason why later(overwrites/no matching letter)
        return False

    for r in range(len(word)):
        if board[firstpos+r][col] != word[r] and board[firstpos+r][col] != blank:
            return False

    else:
        return True

def horizontalCheck(board, word, position, row, col): #function to check if a word can be placed horizontally legally
    firstpos = col-position

    if board[row-1][col+1] != blank or board[row+1][col+1] != blank: #ensures that board does not create illegal adjacencies
        return False

    if board[row-1][col-1] != blank or board[row+1][col-1] != blank: #ensures that board does not create illegal adjacencies
        return False

    elif board[row][col+1] != blank or board[row][col-1] != blank: #ensures that word does not overwrite words on board, print reason why later
        return False

    for c in range(len(word)):
        if board[row][firstpos+c] != word[c] and board[row][firstpos+c] != blank:
            return False

    else:
        return True
    
def placeword(board, word): #function to place words on grid
    placed = False
    match = False

    for letter in range(len(word)): #loop that checks through the entire grid for words that can potentially intersect with the next word in the wordList
        for i in range(20):
            for j in range(20):
                if word[letter] == board[i][j]:
                    match = True
                    pos = word.index(word[letter])

                    if verticalCheck(board,word,pos,i,j):
                        for n in range(len(word)):
                            board[i-pos+n][j] = word[n]
                        placed = True

                    elif horizontalCheck(board,word,pos,i,j):
                        for n in range(len(word)):
                            board[i][j-pos+n] = word[n]
                        placed = True
                    
                if placed: #breaks loop if word is placed so that the same word is not placed multiple times
                    break

    if match == False: #lets the user know which word was not placed due to unmatchability
        print(word, "- no matching letter found")
        print('\n')
    
    elif placed == False: #lets the user know which word was not placed due to an illegal adjacency
        print(word, "- illegal adjacency")
        print('\n')
                    
    return board

def crossword(board, wordList): #function to print crossword onto the grid
    bL = len(board)
    index = 0
    wL = len(wordList[index])
    illegalWords = []

    #removing oversized words from list
    for word in wordList: 
        if len(word) > 20:
            illegalWords.append(word)
            wordList.remove(word)

    #lets the user know which words are oversized
    if len(illegalWords) > 0:
        print("The following word(s) could not be placed because they reach outside of the grid", illegalWords)
        print('\n')

    #placing first word in the center
    if index == 0:
        for k in range(wL):
            column = bL//2 - wL//2 + k               
            board[bL//2][column] = wordList[index][k]
        index +=1

    #places words in list on the board
    while index < len(wordList):
        placeword(board, wordList[index])
        index +=1

    return board
printboard(crossword(board,['hippopotamus','dragon','need','ogre','dare','marathon','headphones','rage','xylophone','zzzz']))

#example inputs:
                    #['clowning','apple','addle','incline','plane','loon']))
                    #['xxxxxxxx','zzzzzzz']))
                    #['hippopotamus','dragon','need','ogre','dare', 'marathon', 'headphones','rage','xylophone','zzzz']))

