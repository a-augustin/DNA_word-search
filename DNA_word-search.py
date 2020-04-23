import numpy as np

# ECE 105: Programming for Engineers II (Spring, 2020)
# HW : DNA Word Search
# Student name:     Alisha Augustin  
# Email ID:         aia43              

def find(word):
    global numRows, numCols
    numRows = board.shape[0]
    numCols = board.shape[1]
    
    for i in range(0,numCols):
        Colstring = ''.join(board[:,i])
        if word in Colstring or word in Colstring[::-1]:
            return True
        
    for i in range(0,numRows):
       Rowstring = ''.join(board[i,:])
       if word in Rowstring or word in Rowstring[::-1]:
            return True

    for i in range(-5,4):
        Diagstring = ''.join(np.diagonal(board, i))
        if word in Diagstring or word in Diagstring[::-1]:
            return True      
        
    for i in range(-5,4):
        DiagRevstring = ''.join(np.diagonal(np.fliplr(board), i))
        if word in DiagRevstring or word in DiagRevstring[::-1]:
            return True        
    else:
        return False
        
    return any([checkRows(word), checkCols(word), checkDiagsFor(word), checkDiagsRev(word)]) 
       
def checkRows(word):
    return any([checkRow(i,word) for i in range(numRows)])

def checkCols(word):
    return any([checkCol(i,word) for i in range(numCols)])

def checkDiagsFor(word):
	return any([checkDiagFor(i, word) for i in range(numRows+1, numCols)])

def checkDiagsRev(word):
	return any([checkDiagRev(i, word) for i in range(numRows+1, numCols)])

def checkRow(i, word):
    extractedArray = board[i,:]
    string = ''.join(board[i,:])[1:-1]
    print('\n--- Debug check at checkRow(i, word) where i = {} ---'.format(i))
    print('Extracted array is:  \t', extractedArray)  
    return checkRCD(string,word)

def checkCol(i, word):
    extractedArray = board[:,i] 
    string = ''.join(extractedArray)[1:-1]
    print('\n--- Debug check at checkCol(i, word) where i = {} ---'.format(i))
    print('Extracted array is:  \t\t', extractedArray)    
    return checkRCD(string,word)

def checkDiagFor(i, word): 
    extractedArray = np.diagonal(board, i)
    string = ''.join(extractedArray)
    print('\n--- Debug check at checkDiagFor(i, word) where i = {} ---'.format(i))
    print('Extracted array is:  \t\t', extractedArray)
    return checkRCD(string,word)

def checkDiagRev(i, word):
    extractedArray = np.diagonal(np.fliplr(board), i) 
    string = ''.join(extractedArray)[1:-1]
    print('\n--- Debug check at checkDiagRev(i, word) where i = {} ---'.format(i))
    print('Extracted array is:  \t', extractedArray) 
    return checkRCD(string,word)

def checkRCD(string, word):
    wordRev = ''.join(reversed(word))
    print('Extracted string is: \t\t {}'.format(string))
    print('Target word and its reverse: \t {}\t{}'.format(word, wordRev))
    # Use string membership to check if word is in extracted string
    wordIsFound = word in string         
    # Use string membership to check if reverse is in extracted string
    reverseIsFound = wordRev in string
    if wordIsFound:
        print('\t**********************************')
        print('\t*  Found match non-flipped word  *')
        print('\t**********************************')
        
    if reverseIsFound:
        print('\t******************************')
        print('\t*  Found match flipped word  *')
        print('\t******************************')

    if word in string or wordRev in string:
        return True 
    else:
        return False
# --- COMPLETE THE FIND FUNCTION ABOVE --------------------------------------



# --- YOU MAY TEST YOUR CODE BELOW ------------------------------------------
if __name__ == '__main__':   # check if run this script as the main file
    # If run this Python script file as the main file, then do following tests
    # else (e.g. when import this script into another file), the following 
    #   code will be skipped.
    
    # --- Example test setup 1: for testing the whole function "find"
    board = np.array([['A','A','A','T'],
                      ['A','G','G','C'],
                      ['A','T','G','C'],
                      ['A','A','T','A'],
                      ['A','T','A','A']])
    #word = 'ACCT' # Expect True, ACCT is at the last column, read upward
    #word = 'CTT'  # Expect True, CTT is at anti diag, SouthWest direction
    #word = 'ATTA'  # Expect True, ATTA is at diag, SouthEast direction
    #word = 'AAA' # Expect True, found in many directions and locations
    #word = 'TTTA' # Expect False, not anywhere
    word = 'TTTAGCTA' # Expect False, not anywhere, also too long
    
    print('=== Test case starts ===========================================')
    result = find(word) 
    print(board)
    print('*** Target word:', word, '\tResult:', result)
    print('=== Test case ends ===========================================')
    
    
    # --- Example test setup 2: for testing individual subtasks
    #     such as "checkDiagFor" function (if you have one)
    # board = np.array([['A','A','A','T'],
    #                   ['A','G','G','C'],
    #                   ['A','T','G','C'],
    #                   ['A','A','T','A'],
    #                   ['A','T','A','A']])
    # print('*** Result 1: ', checkDiagFor(0,'AGGA') ) # True
    # print('*** Result 2: ', checkDiagFor(1,'AGGA') ) # False
    # print('*** Result 3: ', checkDiagFor(1,'CGA') )  # True
    
    
    
    