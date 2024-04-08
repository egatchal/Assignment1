from collections import defaultdict

def tokenize(textFilePath):
    """Tokenizes the input text file
    
    Parameters
    ----------
    textFilePath : str 
        the text file path to read from
    
    Returns
    -------
    list
        a list of tokens read from the input file
    """
    
    try:
        with open(textFilePath, "r") as f:
            text = f.read().lower()
    except FileNotFoundError:
        return []
    
    tokens = []
    token = ""
    
    for c in text:
        if (c.isalnum()): # check if character is alphanumeric and add to token
            token += c
        elif (token == ""): # if token is empty string do not add to tokens
            continue
        else:
            tokens.append(token) # if token is not empty string add to tokens
            token = ""
    
    if token != "": # if last token is not empty string add to tokens
        tokens.append(token)
    
    return tokens

def computeWordFrequencies(tokens):
    """Compute the frequency of tokens
    
    Parameters
    ----------
    tokens : list
        list of tokens
    
    Returns
    -------
    dict
        a dictionary containing a token (key) and count (value) key-value pair
    """
    frequencies = defaultdict(int)
    for token in tokens:
        frequencies[token] += 1
    return frequencies

def printFrequencies(frequencies):
    """print the frequency of tokens in sorted order
    
    Parameters
    ----------
    tokens : dict
        frequency of tokens
    """
    frequencies = sorted(frequencies.items(), key=lambda x: (x[1],x[0]), reverse=True) # sort by value then key in descendding order
    for token, count in frequencies:
        print(f"{token}\t{count}")

if __name__ == "__main__":
    tokens = tokenize("/Users/einargatchalian/Downloads/sheesh.txt")
    #print(tokens)
    frequencies = computeWordFrequencies(tokens)
    #print(frequencies)
    printFrequencies(frequencies)