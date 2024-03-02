from src.Vacancy import Vacancy
import pytest
import json

@pytest.fixture
def example_one():
    return Vacancy('Технический директор', '120000-130000', 'https://url1', 'опыт работы, высшее образование.')

@pytest.fixture
def example_two():
    return Vacancy('Python-разработчик', '60000-70000', 'https://url21', 'любовь к разработке, стрессоустойчивость.')

def test_repr(example_one):
    assert example_one.__repr__() == 'Технический директор: 120000-130000, опыт работы, высшее образование., https://url1'

def test_lt(example_one, example_two):
    assert example_one.__lt__(example_two) == False

def test_gt(example_one, example_two):
    assert example_one.__gt__(example_two) == True



