def hashFunction(key):
    myHash = 0
    for letter in key:
        myHash = (myHash + ord(letter) * 19)
    return myHash

hashFunction("apple")