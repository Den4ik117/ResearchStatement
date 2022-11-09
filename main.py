from research.users import Users
from var_dump import var_dump


if __name__ == '__main__':
    filename = 'data/statement.csv'
    users = Users.import_from_csv(filename)
    filtered_users = users.filter(lambda user: not user.elearn)

    for user in filtered_users:
        print('{0:.<40} | Итог: {1:>2} |'.format(user.full_name, user.total))
    print('-' * 53)
    print('Всего пользователей найдено: {0}'.format(len(filtered_users)))
