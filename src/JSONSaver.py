import json
from abc import ABC, abstractmethod
import os


class GetVacancyInfo(ABC):
    """Абстрактный класс для работы с информацией о вакнсиях"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_info(self):
        pass


class JSONSaver(GetVacancyInfo):
    """Сохраняет информацию в json-файл и позволяет с ним взаимодействовать"""

    file_path = os.path.join('data', 'vacancies_list.json')

    def __init__(self):
        """Создает json-file"""
        self.file_path = os.path.join('data', 'vacancies_list.json')

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в созданный файл"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancy.__dict__, file)

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из файла"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            data = json.load(file)
            for element in data:
                if element == vacancy.__dict__:
                    del element

    def get_info(self):
        pass
