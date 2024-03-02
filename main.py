from src.HHVacanciesList import HHVacanciesList
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
from src.functions import filter_vacancies, get_vacancies_by_salary, get_top_vacancies, print_vacancies


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    salary_range = input("Введите диапазон зарплат (пример: 10000-40000): ")
    top_n = int(input("Введите количество вакансий для вывода в топ: "))

    # Создаем экземпляр класса для работы с вакансиями
    hh_api = HHVacanciesList(search_query)

    # Получаем вакансии в формате json и преобразуем в список объектов
    hh_vacancies = hh_api.get_vacancies()
    vacancies_list = Vacancy.cast_to_list(hh_vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sorted(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
   user_interaction()

