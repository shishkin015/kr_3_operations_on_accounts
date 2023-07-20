import json

from utils.Transactionspy import Transactions


def transforms_operations(filename: json) -> list:
    """
    The function returns a list from a JSON file
    """
    with open(filename, "r") as file:
        return json.load(file)


def returns_executed(data_list: list) -> list:
    operations = []

    for operation in data_list:
        try:
            if operation["state"] == "EXECUTED":
                operations.append(operation)
        except KeyError:
            continue

    last_five_surgeries = sorted(operations, key=lambda x: x['date'], reverse=True)
    return last_five_surgeries


def production_elements_operations(last_five_surgeries: list) -> list:
    for element in last_five_surgeries:
        date = element["date"]
        description = element["description"]
        state = element["state"]
        operation_id = int(element["_id"])
        sum_operation = float(element["operationAmount"]['amount'])
        currency = element["operationAmount"]['currency']["name"]
        destination = element["to"]

        element = Transactions(date, description, state, operation_id, sum_operation, currency, destination)

    return last_five_surgeries
