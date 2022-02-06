def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    import random
   
    
    success  =[]
    balls = [1, 1, 1, 2, 2, 2]
    for i in range(numTrials):
        results = random.sample(balls, 3)
        print(balls, results)
        if len(set(results)) == 1:
            success.append(1)
    return len(success)/numTrials

print(noReplacementSimulation(80000))