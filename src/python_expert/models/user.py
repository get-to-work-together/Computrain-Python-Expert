from dataclasses import dataclass
from enum import Enum
import hashlib
import random
import string


class InvalidPasswordException(Exception):
    pass


class Role(Enum):
    READ = 1,
    MODIFY = 2,
    ADMIN = 9


@dataclass
class User:
    name: str
    e_mail: str
    group: str|None = None
    active: bool = True
    role: Role = Role.ADMIN
    password_hash: str = 'NOT PROVIDED YET'
    salt: str = ''.join(random.choices(string.ascii_letters, k=10))

    def __str__(self):
        return f'User: {self.name} - {self.e_mail}'

    @staticmethod
    def is_valid_password(password):
        is_long_enough = len(password) >= 6
        return is_long_enough

    def set_password(self, password: str):
        if User.is_valid_password(password):
            m = hashlib.sha256()
            m.update((password + self.salt).encode())
            self.password_hash = m.hexdigest()
        else:
            raise InvalidPasswordException('InvalidPassword')

    def check_password(self, password: str) -> bool:
        m = hashlib.sha256()
        m.update((password + self.salt).encode())
        return m.hexdigest() == self.password_hash


if __name__ == '__main__':

    user1 = User('Peter', 'peter@tip.nl')
    print(user1)

    user1.set_password('Welkom01!')
    print(user1.password_hash)

    if user1.check_password('Welkom01!'):
        print('Correct Password')
    else:
        print('Incorrect Pasword')

    if user1.check_password('HACKER!'):
        print('Correct Password')
    else:
        print('Incorrect Pasword')
