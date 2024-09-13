# ## Generators :
# ## yield creates generators.
# def get_numbers():
#     yield 1
#     yield 2
#     yield 3

# ##
# for i in get_numbers():
#     print(i)

# ##
# print(get_numbers())

# ## Named tupless

# from collections import namedtuple

# #                              type_name [field_names]
# Person = namedtuple('Person', ['name', 'age' ,'city'])

# pt = Person('suru','20','Blr')
# print(pt.name)
######################################################
import datetime
maper = lambda x : x.split('/')
print(maper('10/5/2016'))

def maper(x):
    li = x.split('/')
    return int(li[2]),int(li[1]),int(li[0])

maper = lambda x: tuple(int(i) for i in x.split('/')[::-1])
print(maper('10/5/2016'))

print(datetime.datetime(*maper('10/5/2016')))