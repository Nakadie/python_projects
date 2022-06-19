test = "()()()()()()()())("
def parenbalanced(parens):
    for i in range(int(len(parens)/2)):
        parens = parens.replace('(', '', 1)
        parens = parens.replace(')', '', 1)
        print(parens)
        if parens == "()":
            print("true")
            return True
    if parens != "()":
        print("false")
        return False



    


parenbalanced(test)