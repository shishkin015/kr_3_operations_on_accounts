import json


def transforms_operations(filename: json) -> list:
    """
    The function returns a list from a JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)


def returns_executed(data: list) -> list:
    details = []

    for operations in data:
        try:
            if operations["state"] == "EXECUTED":
                details.append(operations)
        except KeyError:
            continue

    last_five_surgeries = sorted(details, key=lambda operations: operations['date'], reverse=True)

    return last_five_surgeries[:5]
