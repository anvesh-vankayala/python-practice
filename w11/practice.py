### Lazy loading in a class with properties.
import math

class Circle:

    def __init__(self, r) -> None:
        self._radius = r
        self._area = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area == None:
            self._area = math.pi * self._radius ** 2
            print(f'recomputed area : with new radius {self._radius}')
            return self._area
        else:
            return self._area



cle = Circle(3)
print(cle.area)
print(cle.area)
cle.radius = 10
print(cle.area)

print('...............................')
cle = Circle(5)
print(cle.area)

#########################################################################################################
## Counter - which can be alternate for 'range'
def counter(start,end):
    start-=1 ## To start with same given value.
    end-=1 ## End value would be excluded. (similar to range)
    def inner():
        nonlocal start
        nonlocal end
        if start < end:
            start+=1
            return start
        else:
             raise StopIteration()
    return inner

cnt = counter(0,5)

for i in range(0,5):
    try:
        print(cnt())
    except Exception as e:
        print(e)
