class Square():

    def __init__(self,
                 length):

        self.length = length
        self.i = 0

    def __iter__(self): ## Object can only be made iterable, by implementing this method
        return self

    def __next__(self):
        if self.i > self.length:
            raise StopIteration('i is greater then given length')
        rtn_val = self.i ** 2
        self.i+=1
        return rtn_val
    
#####################################
# sq = Square(100)

# # while(True):
# #     print(next(sq))

# [print(i, end='\t') for i in sq]
#####################################


## As we need to recreate the object to restart the iterable.
## To use it as default iterable like list and set, we will create a class inside the class, and return that object.
## So when ever we call the Object, new inner object will be returned and gets the list from first.


class Square:

    def __init__(self,
                 length):
        self.length = length

    def __iter__(self):
        return self.SquareIterator(self)

    class SquareIterator():

        def __init__(self,sq_obj):

            self.length = sq_obj.length
            self.i = 0

        def __iter__(self): ## Object can only be made iterable, by implementing this method
            return self

        def __next__(self):
            if self.i > self.length:
                raise StopIteration('i is greater then given length')
            rtn_val = self.i ** 2
            self.i+=1
            return rtn_val

#####################################

sq = Square(5)

print(id(sq.__iter__), id(iter(sq)))
print(id(sq.__iter__), id(iter(sq)))

[print(i,end='\t') for i in sq]


#####################################
