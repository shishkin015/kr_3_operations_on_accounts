import json


def transforms_operations(filename: json) -> list:
    """
    The function returns a list of the last 5 operations from the JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
