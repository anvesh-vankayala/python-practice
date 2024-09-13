## Generators :
## yield creates generators.
def get_numbers():
    yield 1
    yield 2
    yield 3

##
for i in get_numbers():
    print(i)

##
print(get_numbers())

## Named tupless

from collections import namedtuple

#                              type_name [field_names]
Person = namedtuple('Person', ['name', 'age' ,'city'])

pt = Person('suru','20','Blr')
print(pt.name)