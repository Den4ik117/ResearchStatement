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
        return Users(list(sorted(self._users, key=function, reverse=reverse)))

    def filter(self, function):
        return Users(list(filter(function, self._users)))

    def __iter__(self):
        for user in self._users:
            yield user

    def __len__(self):
        return len(self._users)

    def get(self, count):
        return Users(self._users[:count])

    def group(self, key):
        group_users = GroupUsers()
        for user in self._users:
            group_users[getattr(user, key)] = user
        return group_users
    
    def contribution_by_keys(self, *keys) -> dict[str, int]:
        counter = {key: [] for key in keys}
        for user in self._users:
            for key in keys:
                counter[key].append(getattr(user, key))
        return {key: sum(values) / len(values) for key, values in counter.items()}


class GroupUsers:
    def __init__(self):
        self._users: dict[str, Users] = {}

    def __setitem__(self, key: str, value: User) -> None:
        if key in self._users:
            self._users[key].append(value)
        else:
            self._users[key] = Users([value])

    def __getitem__(self, item: str) -> Users:
        return self._users[item]

    def __len__(self):
        return len(self._users.keys())

    def keys(self) -> list[str]:
        return list(self._users.keys())

    def values(self) -> list[Users]:
        return list(self._users.values())

    def sort_keys(self, reverse=True):
        tuple_group_users = [(key, values) for key, values in self._users.items()]
        tuple_group_users.sort(key=lambda users: users[0], reverse=reverse)
        self._users = dict(tuple_group_users)
        return self

    def sort_values(self, reverse=True):
        tuple_group_users = [(key, values) for key, values in self._users.items()]
        tuple_group_users.sort(key=lambda users: len(users[-1]), reverse=reverse)
        self._users = dict(tuple_group_users)
        return self
