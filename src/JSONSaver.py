import json
from abc import ABC, abstractmethod
import os


class GetVacancyInfo(ABC):
    """Абстрактный класс для работы с информацией о вакнсиях"""

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

    @abstractmethod
    def get_info(self, *args):
        pass


class JSONSaver(GetVacancyInfo):
    """Сохраняет информацию в json-файл и позволяет с ним взаимодействовать"""

    def __init__(self):
        """Создает json-file"""
        file_path = os.path.join('data', 'vacancies_list.json')
        with open(file_path, 'w', encoding='utf-8') as file:
            self.file = 'vacancies_list.json'


    def add_vacancy(self, vacancy):
        """Добавляет вакансию в созданный файл"""
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(vacancy, file)


    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из файла"""
        with open(self.file, 'rw', encoding='utf-8') as file:
            data = json.load(file)
            for element in data:
                if element == vacancy:
                    del element

    def get_info(self, *args):
        pass









