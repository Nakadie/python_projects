import math
def polysum(n,s):
    '''
    

    sum the area and square of the perimeter of the regular polygon.
    ----------
    n : an intiger, number of sides.
    s : an intiger, length of sides.

    Returns
    -------
     returns the sum, rounded to 4 decimal places.

    '''
    pi = 3.14159265359
    area = ((.25*n*(s**2))/(math.tan(pi/n)))
    perimiter = s*n
    return round(area + (perimiter**2), 4)
    
n=86
s=14
answer =1564921.4587
print(polysum(n, s))