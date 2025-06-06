
class Person:

    # __slots__ = ('_name', '_residence')

    def __init__(self, name, residence = 'unknown'):
        self._name = name
        self._residence = residence

    def tell(self):
        return f'I am {self._name} and I live in {self._residence}'
    
    def move(self, new_residence):
        self._residence = new_residence

# --------------------------------------------------------------------

p = Person('Albert', 'Amsterdam')
print( p.tell() )
p.move('Eindhoven')
print( p.tell() )

print(p.__dict__)