# class Breuk:

#     def __init__(self, teller: int, noemer: int):
#         """Een breuk met teller/noemer"""
#         self._teller = teller
#         self._noemer = noemer

#     def __repr__(self):
#         return f'{self._teller}/{self._noemer}'

#     def __add__(self, other):
#         return Breuk(self._teller * other._noemer + other._teller * self._noemer, self._noemer * other._noemer)

#     def __mul__(self, other):
#         return Breuk(self._teller * other._teller, self._noemer * other._noemer)




from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Breuk:
    _teller: int|float = 1
    _noemer: int|float = 1

    def __str__(self):
        return f'{self._teller}/{self._noemer}'

    def __add__(self, other):
        return Breuk(self._teller * other._noemer + other._teller * self._noemer, self._noemer * other._noemer)

    def __mul__(self, other):
        return Breuk(self._teller * other._teller, self._noemer * other._noemer)

    def vereenvoudig(self):
        ggd = math.gcd(self._teller, self._noemer)
        return Breuk(self._teller / ggd, self._noemer / ggd)

    # Factory methods

    @staticmethod
    def from_string(s: str):
        s1, s2 = s.split('/')
        return Breuk(int(s1), int(s2))

    # @classmethod
    # def from_string(cls, s: str):
    #     s1, s2 = s.split('/')
    #     return cls(int(s1), int(s2))


if __name__ == '__main__':

    breuk1 = Breuk(3, 8)
    breuk2 = Breuk(1, 4)

    print(breuk1)
    print(breuk2)

    breuk3 = breuk1 + breuk2
    print(breuk3)
    print(breuk3.vereenvoudig())

    s = '2/3'
    breuk3 = Breuk.from_string(s)
    print(breuk3)