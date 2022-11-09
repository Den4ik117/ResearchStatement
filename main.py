from research.users import Users
from jinja2 import Environment, FileSystemLoader
from research.writer import write
from datetime import datetime


if __name__ == '__main__':
    filename = 'data/statement.csv'
    template_folder = 'templates'
    template = 'report_template.html'

    users = Users.import_from_csv(filename)

    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template(template)
    html_template = template.render({
        'date': datetime.today().strftime('%d.%m.%Y'),
        'users1': users.filter(lambda user: user.elearn and user.contest).sort(lambda user: user.total, True).get(10),
        'users2': users.filter(lambda user: not(user.elearn and user.contest)).sort(lambda user: user.total, True),
    })

    write('templates/report.html', html_template)
