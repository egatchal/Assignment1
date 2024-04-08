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
    
    with open(textFilePath, "r") as f:
        text = f.read().lower()
    
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

if __name__ == "__main__":
    tokens = tokenize("/Users/einargatchalian/Downloads/sheesh.txt")
    print(tokens)