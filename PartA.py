def tokenize(textFilePath):
    with open(textFilePath, "r") as f:
        text = f.read().lower()
    
    tokens = []
    token = ""
    
    for c in text:
        if (c.isalnum()):
            token += c
        elif (token == ""):
            continue
        else:
            tokens.append(token)
            token = ""
    
    if token != "":
        tokens.append(token)
    
    return tokens

if __name__ == "__main__":
    tokens = tokenize("/Users/einargatchalian/Downloads/sheesh.txt")
    print(tokens)