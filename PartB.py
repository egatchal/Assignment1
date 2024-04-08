import sys
from PartA import tokenize, computeWordFrequencies

def intersection(textFilePath1, textFilePath2):
    """print the tokens shared between two text files
    
    Parameters
    ----------
    textFilePath1 : str
        path name for text file 1
    textFilePath2 : str
        path name for text file 2
    """

    tokens1 = tokenize(textFilePath1) # get tokens for first file
    tokens2 = tokenize(textFilePath2) # get tokens for second file
    
    frequencies1 = computeWordFrequencies(tokens1) # get token count for first file
    frequencies2 = computeWordFrequencies(tokens2) # get token count for second file
    
    intersecting_tokens = []
    
    for token in frequencies1:
        if token in frequencies2: # get the shared tokens
            intersecting_tokens.append(token)
    
    for token in intersecting_tokens:
        print(token)
    
    print(len(intersecting_tokens))

if __name__ == "__main__":
    '''
    tFP1: /Users/einargatchalian/Desktop/CS121/test1.txt 
    tFP2: /Users/einargatchalian/Desktop/CS121/test2.txt
    '''
    if len(sys.argv) == 3:
        textFilePath1 = sys.argv[1]
        textFilePath2 = sys.argv[2]
        intersection(textFilePath1, textFilePath2)
    else:
        print("Error missing text file path(s).")