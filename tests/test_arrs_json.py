from utils.arrs_json import *


def test_transforms_operations(open_json):
    path, result = open_json
    assert transforms_operations(path) == result


def test_production_elements_operations(operation_elements_from_the_list):
    positive_test_list, result_list = operation_elements_from_the_list
    positive_test_list = production_elements_operations(positive_test_list)

    assert result_list[0].operation_id == positive_test_list[0].operation_id
    assert result_list[1].operation_id == positive_test_list[1].operation_id


def test_sorts_the_list_by_date(sort_elements_from_the_list):
    positive_test_list, result_list = sort_elements_from_the_list
    positive_test_list = sorts_the_list_by_date(positive_test_list)

    assert result_list[0].operation_id == positive_test_list[0].operation_id
    assert result_list[1].operation_id == positive_test_list[1].operation_id
