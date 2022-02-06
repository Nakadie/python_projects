s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
def printer_error(s):
    errors = 0
    string = s
    good_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    error_letters = ['n','o','p', 'q','r','s','t','u','v','w','x','y','z']
     
    for i in error_letters:
        if i in s:
            errors += s.count(i)
        else:
            pass
    return ((str(errors))) + '/' + str(len(s))

print(printer_error(s))