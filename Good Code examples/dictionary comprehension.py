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




var = "one two three four".split()
def chunk(lst): yield [lst[i:i + 2] for i in range(0, len(lst), 2)]
print(dict(list(chunk(var))[0]))


# The chunk thing basicly do this: "one two three four" → [[["one", "two"], ["three", "four"]]].
# Or the chunk is a generator, then we use list() on that, and then dict() on the list.
# Or even before that we need to do [0] on the list to get the list of lists.