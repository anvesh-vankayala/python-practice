import math

class Polygon:

    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices')
        self._n = n ## No. vertices
        self._R = R ## Circum radius

    def __repr__(self) -> str:
        return f'Ploygon(n={self._n}, R = {self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angles(self):
        return (self._n - 2) * 180 / self._n
    
    @property
    def side_length(self):
        return 2 * self._R *math.sin(math.pi/ self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self,other):
        if isinstance(other , self.__class__):
            return (self.count_edges == other.count_edges and 
                    self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self,other):
        if isinstance(other,self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
        
# print(Polygon(3,10))