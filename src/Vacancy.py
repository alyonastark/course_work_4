
class Vacancy:
    """Класс для работы с вакансиями(сравнениие и валидация данных)"""

    all_vacancies = []

    def __init__(self, title, salary, url, requirement):
        self.title = title
        self.salary = salary
        self.url = url
        self.requirement = requirement


    @classmethod
    def cast_to_list(self, vacancies):
        """Преобразует информацию из формата json в список"""
        self.all_vacancies.clear()
        for vacancy in vacancies:
            title = vacancy['name']
            if vacancy['salary'] is None:
                salary = 0
            elif vacancy['salary']['to'] is None:
                salary = f'{vacancy['salary']['from']}'
            elif vacancy['salary']['from'] is None:
                salary = f"0-{vacancy['salary']['to']}"
            else:
                salary = f"{vacancy['salary']['from']}-{vacancy['salary']['to']}"
            url = vacancy['url']
            requirement = vacancy['snippet']['requirement']
            vacancy_main_data = Vacancy(title, salary, url, requirement)
            self.all_vacancies.append(vacancy_main_data)
        return self.all_vacancies

    # def __sub__(self, other):
    #     """метод для сравнения по зп(по нижней границе)"""
    #     if isinstance(other, Vacancy):
    #         first_salary = int(self.salary.split('-')[0])
    #         second_salary = int(other.salary.split('-')[0])
    #         return first_salary - second_salary

    def __lt__(self, other):
        """метод для сравнения по зп(по нижней границе)"""
        if isinstance(other, Vacancy):
            first_salary = int(self.salary.split('-')[0])
            second_salary = int(other.salary.split('-')[0])
            return first_salary < second_salary


    def __le__(self, other):
        """метод для сравнения по зп(по нижней границе)"""
        if isinstance(other, Vacancy):
            first_salary = int(self.salary.split('-')[0])
            second_salary = int(other.salary.split('-')[0])
            return first_salary <= second_salary


    def __gt__(self, other):
        """метод для сравнения по зп(по нижней границе)"""
        if isinstance(other, Vacancy):
            first_salary = int(self.salary.split('-')[0])
            second_salary = int(other.salary.split('-')[0])
            return first_salary > second_salary


    def __ge__(self, other):
        """метод для сравнения по зп(по нижней границе)"""
        if isinstance(other, Vacancy):
            first_salary = int(self.salary.split('-')[0])
            second_salary = int(other.salary.split('-')[0])
            return first_salary >= second_salary





