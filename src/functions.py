

def filter_vacancies(vacancies, filter_words):
    """Фильтрует вакансии по ключевым словам в требованиях"""
    filtered_vacancies = []
    for vacancy in vacancies:
        if filter_words.lower() in vacancy.title.lower():
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Выдает список вакансий с указанным диапазоном зп"""
    suitable_vacancies = []
    for vacancy in filtered_vacancies:
        salary = vacancy.salary
        range = salary_range.split('-')
        if int(salary.split('-')[0]) >= int(range[0]):
            try:
                int(salary.split('-')[1]) >= int(range[1])
            except IndexError:
                suitable_vacancies.append(vacancy)
        suitable_vacancies.append(vacancy)
    return suitable_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """Выдает n количество лучших вакансий"""
    top_vacancies = []
    try:
        for i in range(top_n):
            top_vacancies.append(sorted_vacancies[i])
    except IndexError:
        pass
    return top_vacancies


def print_vacancies(vacancies):
    """Выводит отобранные вакансии"""
    for vacancy in vacancies:
        vacancy_dict = vacancy.__dict__
        for value in vacancy_dict:
            print(vacancy_dict[value])
