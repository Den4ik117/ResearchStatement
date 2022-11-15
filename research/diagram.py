import matplotlib.pyplot as plt
import numpy as np
from research.utils import percent_autopct, english_keys_to_russian_description


def make_first_diagram(users):
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


def make_second_diagram(users):
    result = users.contribution_by_keys('openedu', 'practices', 'activities', 'project')

    values = list(result.values())
    labels = [english_keys_to_russian_description[key] for key in result.keys()]

    fig, ax = plt.subplots()
    ax.set_title('Средний вклад той или иной активности в итоговый результат')
    ax.pie(values, labels=labels, autopct=percent_autopct(values))

    plt.savefig('images/image_2.png')


def make_third_diagram(users):
    nested_users = users.group('teacher').sort_values(reverse=False)

    labels1 = nested_users.keys()
    values1 = [len(users) for users in nested_users.values()]

    x = np.arange(len(labels1))
    width = 0.8
    xlabels = np.arange(0, values1[-1] + 20, 20)

    fig, ax = plt.subplots()

    ax.barh(x, values1, width, label=labels1)
    ax.set_title('Преподаватели и количество их подданных')
    ax.set_xlabel('Количество студентов')
    [ax.text(values1[i] + 0.4, i, values1[i], ha='left', va='center', fontsize=8) for i in range(len(labels1))]
    ax.set_yticks(x, labels1, fontsize=6)
    ax.set_xticks(xlabels, xlabels, fontsize=8)
    ax.grid(axis='x')
    fig.tight_layout()

    plt.savefig('images/image_3.png')
