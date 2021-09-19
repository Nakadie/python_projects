def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    abc = sorted(aStr)
    if  not aStr:
      return False
    
    else:
        cut = abc[len(abc)//2]
        if char == abc or char == cut:
            return True
        elif char > cut:
            return isIn(char, abc[1:])
        elif char < cut:
            return isIn(char, abc[:-1])
    
        

    
    
    
print(isIn('a', 'fgjkdfjkfgdjk'))