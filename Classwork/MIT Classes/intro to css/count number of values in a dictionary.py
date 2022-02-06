animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    loop = 0
    while loop <= (len(animals.keys())):
        for x in aDict:
            if len(animals[x]) >1:
                for y in range(len(animals[x])):
                    count += 1
            else: 
                count += 1
        loop += 1
        return count
    
print(how_many(animals))