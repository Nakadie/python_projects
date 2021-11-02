# class Strict(object):
    
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return self.string

#     def name(self):
#         if len(self.string) == 5:
#             return print(self.string)
#         else:
#             return print('Name must be exactly 5 characters')


# blah = Strict('abcde')
# blah.name()

class Strict(object):
    def __init__(self, name):
        self.name = name
    
    def name_of_user(self):
        if len(self.name) != 5:
            return print('Name must be exactly 5 characters')
        else:
            return print(self.name)

test = Strict('abcde')
test.name_of_user()
