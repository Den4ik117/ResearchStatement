def percent_autopct(values):
    def autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%'.format(p=pct, v=val)

    return autopct


english_keys_to_russian_description = {
    'openedu': 'OpenEdu',
    'project': 'Итоговый\nпроект',
    'activities': 'Активности на\nзанятиях',
    'practices': 'Практики на\nELearn',
}
