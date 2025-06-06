from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass
from sqlalchemy.orm import Session

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


class Base(DeclarativeBase):
    """subclasses will be converted to dataclasses"""
    pass


class User(MappedAsDataclass, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    e_mail: Mapped[str]
    group: Mapped[str] = mapped_column(default=None)
    active: Mapped[bool] = mapped_column(default=True)
    role: Role = mapped_column(default=Role.ADMIN)
    password_hash: Mapped[str] = mapped_column(default='NOT PROVIDED YET')
    salt: Mapped[str] = mapped_column(default=''.join(random.choices(string.ascii_letters, k=10)))

    def __str__(self):
        return f'User: {self.name} - {self.e_mail}'

    @staticmethod
    def is_valid_password(password: str) -> bool:
        is_long_enough = len(password) >= 6
        return is_long_enough
    
    @staticmethod
    def hash_password(password: str, salt: str = '') -> str:
            m = hashlib.sha256()
            m.update((password + salt).encode())
            return m.hexdigest()

    def set_password(self, password: str):
        if User.is_valid_password(password):
            self.password_hash = User.hash_password(password, self.salt)
        else:
            raise InvalidPasswordException('InvalidPassword')

    def check_password(self, password: str) -> bool:
        return self.password_hash == User.hash_password(password, self.salt)


if __name__ == '__main__':

    user1 = User('PeterB', 'peter@tip.nl', group='admin')
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


    DATABASE_URL = 'sqlite:///data/sqlite.db'
    engine = create_engine(DATABASE_URL, echo=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        existing_user = session.query(User).filter_by(e_mail=user1.e_mail).first()
        if existing_user:
            print(f'User with e-mail {user1.e_mail} already exists.')
            existing_user.name = user1.name
            existing_user.group = user1.group
            existing_user.active = user1.active
            existing_user.role = user1.role
            existing_user.password_hash = user1.password_hash
            existing_user.salt = user1.salt
            session.commit()
        else:
            print(f'Adding new user with e-mail {user1.e_mail}.')
            session.add(user1)
            session.commit()

    with Session(engine) as session:
        # result = session.query(User).get(2)
        result = session.query(User).filter_by(name='Peter').first()
        print(result)
