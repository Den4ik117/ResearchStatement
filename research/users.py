from research.user import User
from research.reader import csv_reader


class Users:
    def __init__(self, users=None):
        if users is None:
            users = []
        self._users: list[User] = users

    @staticmethod
    def import_from_csv(filename: str):
        users = Users()
        for row in csv_reader(filename):
            users.append(User(row))
        return users

    def append(self, user: User):
        self._users.append(user)

    def sort(self, function, reverse=False):
        self._users.sort(key=function, reverse=reverse)
        return self

    def filter(self, function):
        return Users(list(filter(function, self._users)))

    def __iter__(self):
        for user in self._users:
            yield user

    def __len__(self):
        return len(self._users)
