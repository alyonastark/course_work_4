from abc import ABC, abstractmethod
import requests
import json


class AbstractApi(ABC):
    """абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def get_vacancies(self):
        pass


class HHVacanciesList(AbstractApi):
    """класс для работы с hh.ru"""

    def __init__(self, vacancy):
        """Инициализатор класса, vacancy - название вакансии для поиска"""
        self.vacancy = vacancy
        self.vacancies = self.get_vacancies()

    def get_vacancies(self):
        """Получает список вакансий"""
        response = requests.get('https://api.hh.ru/vacancies', {
            'text': self.vacancy, 'per_page': 100, 'area': 113})
        vacancies = json.loads(response.text)['items']
        return vacancies
