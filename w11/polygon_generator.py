from polygon import Polygon

def counter(start,end):
    start-=1 ## To start with same given value.
    end-=1 ## To make sure, it does not include end, like range.
    def inner():
        nonlocal start
        nonlocal end
        if start < end:
            start+=1
            return start
        else:
             raise StopIteration()
    return inner



class Polygons:

    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m ## highest polygon vertices
        self._R = R ## Circum radius
        self.count = counter(3,m+1)
        # self._polygons = [Polygon(i,R) for i in range(3,m+1)]
        
    # def __len__(self):
    #     return self._m - 2
    
    def __repr__(self) -> str:
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __iter__(self):
        return self.PolygonIterator(self)
    
    class PolygonIterator:

        def __init__(self,pol_obj) -> None:
            self.i = 0
            self.pol_obj = pol_obj
            self.poly_iter = iter(self.pol_obj._polygons)

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.i > len(self.pol_obj._polygons):  ## it an optinal, even list will have default stop iteration.
                raise StopIteration('i is greater then given length')
            self.i+=1
            return next(self.poly_iter)
    
    # def __getitem__(self,s):
    #     return self._polygons[s]
    
    @property
    def max_efficiency_polugon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p : p.area/p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]

# polys = Polygons(6,10)
# poly_iter = iter(polys)
# print(next(poly_iter))
# print(next(poly_iter))
# print(next(poly_iter))

# [print(i) for i in polys]



# cnt = counter(0,5)

# for i in range(0,5):
#     try:
#         print(cnt())
#     except Exception as e:
#         print(e)
