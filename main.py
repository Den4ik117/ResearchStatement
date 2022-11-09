from research.users import Users
from jinja2 import Environment, FileSystemLoader
from research.writer import write
from datetime import datetime
from var_dump import var_dump
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    filename = 'data/statement.csv'
    template_folder = 'templates'
    template = 'report_template.html'

    users = Users.import_from_csv(filename)

    nested_users = users.group('total').sort_keys(reverse=False)

    labels1 = nested_users.keys()
    values1 = [len(users) for users in nested_users.values()]

    nested_users.sort_values()
    labels2 = nested_users.keys()
    values2 = [len(users) for users in nested_users.values()]

    x = np.arange(len(labels1))
    width = 0.8
    ylabels = np.arange(0, values2[0] + 20, 20)

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.bar(x, values1, width, label=labels1)
    ax1.set_title('Диаграмма количества студентов и их баллов')
    ax1.set_ylabel('Количество студентов')
    ax1.set_xlabel('Количество зелёных баллов')
    [ax1.text(labels1[i], values1[i] + 1, values1[i], ha='center', fontsize=6) for i in range(len(labels1))]
    ax1.set_xticks(x, labels1, fontsize=6)
    ax1.set_yticks(ylabels, ylabels, fontsize=8)
    ax1.grid(axis='y')

    ax2.bar(x, values2, width, label=labels2)
    ax2.set_title('Диаграмма количества студентов и их баллов')
    ax2.set_ylabel('Количество студентов')
    ax2.set_xlabel('Количество зелёных баллов')
    [ax2.text(labels1[i], values2[i] + 1, values2[i], ha='center', fontsize=6) for i in range(len(labels2))]
    ax2.set_xticks(x, labels2, fontsize=6)
    ax2.set_yticks(ylabels, ylabels, fontsize=8)
    ax2.grid(axis='y')

    fig.tight_layout()

    plt.savefig('images/image_1.png')

    # var_dump(nested_users)
    exit()

    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template(template)
    html_template = template.render({
        'date': datetime.today().strftime('%d.%m.%Y'),
        'users1': users.filter(lambda user: user.elearn and user.contest).sort(lambda user: user.total, True).get(10),
        'users2': users.filter(lambda user: not(user.elearn and user.contest)).sort(lambda user: user.total, True),
    })

    write('templates/report.html', html_template)
