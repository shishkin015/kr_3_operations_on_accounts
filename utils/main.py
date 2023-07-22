from utils.arrs_json import *
import os.path



# <дата перевода> <описание перевода>
# <откуда> -> <куда>
# <сумма перевода> <валюта>


if __name__ == '__main__':
    # получаем данные из operations.json
    data_json = transforms_operations(os.path.join("../operations/operations.json"))
    # Фильтрует только выполненные транзакции и сортирует по дате исполнения
    data_json = production_elements_operations(data_json)
    # Обрабатывает детали операций
    data_json = sorts_the_list_by_date(data_json)
    # Выводит последние по дате 5 транзакций
    for transaction in data_json[:5]:
        print(transaction.get_description_operation())
