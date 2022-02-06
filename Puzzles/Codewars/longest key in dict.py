animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['b'].append('dog')
animals['b'].append('dingo')
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    loop = 0
    while True:
        while loop <= (len(animals.keys())):
            for x in aDict:
                if len(animals[x]) >1:
                    count = 0
                    for y in range(len(animals[x])):
                        count += 1
                        maxlen = count
                        loop += 1
                    if count == maxlen:
                        return x
                    
        
        
    if range(len(animals[x])) == maxlen:
            False
print(biggest(animals))
    
