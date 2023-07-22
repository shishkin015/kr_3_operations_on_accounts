import json
import pytest

from utils.Transactions import Transactions
from utils.arrs_json import production_elements_operations


@pytest.fixture(scope='session')
def open_json():
    path = 'F:/PyCharm SkyP/kr_3_operations_on_accounts/tests/test.json'
    with open(path, 'r') as f:
        result = json.load(f)
    return path, result


@pytest.fixture(scope='session')
def operation_elements_from_the_list():
    path = 'F:/PyCharm SkyP/kr_3_operations_on_accounts/tests/test.json'
    with open(path, 'r') as f:
        positive_test = json.load(f)
    result = [
        Transactions(sender='Visa 876543298763232',
                     date='2018-04-04T17:33:34.701093',
                     description='Перевод организации',
                     state='EXECUTED',
                     operation_id=716496732,
                     sum_operation=40701.91,
                     currency='USD',
                     destination='Счет 72731966109147704472'),
        Transactions(sender='Maestro 1596837868705199',
                     date='2019-08-26T10:50:58.294041',
                     description='Перевод с карты на карту',
                     state='EXECUTED',
                     operation_id=441945886,
                     sum_operation=31957.58,
                     currency='руб.',
                     destination='Счет 64686473678894779589')
    ]
    return positive_test, result


@pytest.fixture(scope='session')
def sort_elements_from_the_list():
    path = 'F:/PyCharm SkyP/kr_3_operations_on_accounts/tests/test.json'
    with open(path, 'r') as f:
        positive_test = json.load(f)
    positive_test = production_elements_operations(positive_test)
    result = [
        Transactions(sender='Maestro 1596837868705199',
                     date='2019-08-26T10:50:58.294041',
                     description='Перевод с карты на карту',
                     state='EXECUTED',
                     operation_id=441945886,
                     sum_operation=31957.58,
                     currency='руб.',
                     destination='Счет 64686473678894779589'),
        Transactions(sender='Visa 876543298763232',
                     date='2018-04-04T17:33:34.701093',
                     description='Перевод организации',
                     state='EXECUTED',
                     operation_id=716496732,
                     sum_operation=40701.91,
                     currency='USD',
                     destination='Счет 72731966109147704472')
    ]
    return positive_test, result


@pytest.fixture(scope='session')
def hidden_sender_information():
    return [
        ('Maestro 1596837868700519', 'Maestro 1596 83** **** 0519'),
        ('Visa 1596837868705199', 'Visa 1596 83** **** 5199'),
        ('Мир 1596837868700519', 'Мир 1596 83** **** 0519')
    ]


@pytest.fixture(scope='session')
def hidden_destination_information():
    return [
        ('Счет 1596837868700519', 'Счет **0519'),
        ('Счет 1596837868705199', 'Счет **5199'),
        ('Счет 1596837868700519', 'Счет **0519')
    ]


@pytest.fixture(scope='session')
def date_data():
    return [
        ('2018-04-04T17:33:34.701093', '04.04.2018'),
        ('2019-08-26T10:50:58.294041', '26.08.2019')
    ]


@pytest.fixture(scope='session')
def data_for_operation_description():
    return [
        "07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD",
        "13.11.2019 Перевод со счета на счет\nСчет 3861 14** **** **** 9794 -> Счет **8125\n62814.53 руб."
    ]
