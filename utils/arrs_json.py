import json

from utils.Transactions import Transactions


def transforms_operations(filename: json) -> list:
    """
    Функция возвращает список из файла JSON.
    """
    with open(filename, "r") as file:
        return json.load(file)


def production_elements_operations(data_list: list) -> list:
    """
    Функция разбивает операции на элементы, создает экземпляр класса Transactions,
    и возвращает список объектов класса Transactions
    """
    last_five_surgeries = []

    for element in data_list:

        # Пропустить пустой элемент
        if element == {}:
            continue
        # Игнорировать ошибку с отсутствием значения ключа "from"
        try:
            sender = element["from"]
        except KeyError:
            sender = None
        date = element["date"]
        description = element["description"]
        state = element["state"]
        operation_id = int(element["id"])
        sum_operation = float(element["operationAmount"]['amount'])
        currency = element["operationAmount"]['currency']["name"]
        destination = element["to"]

        # Создаем экземпляр класса Transactions
        element = Transactions(date, description, state, operation_id, sum_operation, currency, destination, sender)

        # Добавляет в список только выполненные операции
        if element.state == "EXECUTED":
            last_five_surgeries.append(element)

    return last_five_surgeries


def sorts_the_list_by_date(last_five_surgeries: list) -> list:
    """
    Сортирует список по дате от ранней даты к поздней
    """
    last_five_surgeries.sort(key=lambda x: x.date, reverse=True)

    return last_five_surgeries


