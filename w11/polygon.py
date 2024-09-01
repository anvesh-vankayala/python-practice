import math

class Polygon:

    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices')
        self._n = n ## No. vertices
        self._R = R ## Circum radius
        self.interior_angles = None
        self.side_length = None
        self.apothem = None
        self.area = None
        self.perimeter = None

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
    
    @count_vertices.setter
    def count_vertices(self, n):
        self.count_vertices = n
        self.interior_angles = None
        self.side_length = None
        self.apothem = None
        self.area = None
        self.perimeter = None

    @circumradius.setter
    def circumradius(self, r):
        self._R = r
        self.side_length = None
        self.apothem = None
        self.area = None
        self.perimeter = None

    @property
    def interior_angles(self):
        if self.interior_angles == None:
            self.interior_angles = (self._n - 2) * 180 / self._n
            print(f'computed interior angles')
        return self.interior_angles
    
    @property
    def side_length(self):
        if self.side_length == None:
            self.side_length =  2 * self._R * math.sin(math.pi/ self._n)
            print(f'computed side length')
        return self.side_length
    
    @property
    def apothem(self):
        if self.apothem == None:
            self.apothem = self._R * math.cos(math.pi / self._n)
            print(f'computed apothme')
        return self.apothem
    
    @property
    def area(self):
        if self.area == None:
           self.area = self._n / 2 * self.side_length * self.apothem
           print(f'computed area')
        return self.area
    
    @property
    def perimeter(self):
        if self.perimeter == None:
            self.perimeter = self._n * self.side_length
            print(f'computed perimeter')
        return self.perimeter
    
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