


class Square():

    def __init__(self,
                 length):

        self.length = length
        self.i = 0

    def __next__(self):
        if self.i > self.length:
            raise StopIteration('i is greater then given length')
        rtn_val = self.i ** 2
        self.i+=1
        return rtn_val
    
#####################################
# sq = Square(5)

# while(True):
#     print(next(sq))
#####################################



