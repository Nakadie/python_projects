#input
'one two three four five six'
#output
{'one': 'two', 'three': 'four', 'five': 'six'}

#ideal code
x='one two three four five six'.split()
print(dict(zip(x[::2],x[1::2])))

#explination
x='one two three four five six'.split()
print(x[::2],x[1::2])
print(tuple(zip(x[::2],x[1::2])))
print(dict(zip(x[::2],x[1::2])))

# importand to know for the future. 
# x[::2] - words in even indices
# x[1::2] - words in odd indices