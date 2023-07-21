from utils.arrs import *
import os.path
# <дата перевода> <описание перевода>
# <откуда> -> <куда>
# <сумма перевода> <валюта>

if __name__ == '__main__':
    # получаем данные из operations.json
    data_json = transforms_operations(os.path.join("../operations/operations.json"))
    # Фильтрует только выполненные транзакции и сортируетпо дате исполнения
    data_json = returns_executed(data_json)
    # Обрабатывает делали операций
    data_json = production_elements_operations(data_json)
    # Выводит последние 5 транзакций
    for transaction in data_json[:4]:
        print(transaction.get_description_operation())
