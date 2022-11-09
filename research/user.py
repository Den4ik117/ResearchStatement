class User:
    def __init__(self, dictionary: dict[str, str]) -> None:
        self.id: str = dictionary['id']
        self.login: str = dictionary['login']
        self.full_name: str = dictionary['full_name']
        self.email: str = dictionary['email']
        self.elearn: bool = True if dictionary['elearn'] == 'Подключен' else False
        self.contest: bool = True if dictionary['contest'] == 'Подключен' else False
        self.team: str = dictionary['team']
        self.teacher: str = dictionary['teacher']
        self.openedu: int = int(dictionary['openedu'])
        self.practices: int = int(dictionary['practices'])
        self.activities: int = int(dictionary['activities'])
        self.project: int = int(dictionary['project'])
        self.total: int = int(dictionary['total'])
