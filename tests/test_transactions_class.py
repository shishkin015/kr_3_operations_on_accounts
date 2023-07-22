from utils.Transactions import Transactions
from utils.arrs_json import production_elements_operations, sorts_the_list_by_date


def test_gets_a_hidden_score_sender(hidden_sender_information):
    for positive_test, result in hidden_sender_information:
        test_value = Transactions("sender", "date", "description", "state", "operation_id", "sum_operation", "currency", positive_test)
        assert test_value.gets_a_hidden_score_sender() == result


def test_get_hidde_beneficiary_account(hidden_destination_information):
    for positive_test, result in hidden_destination_information:
        test_value = Transactions("sender", "date", "description", "state", "operation_id", "sum_operation", positive_test, 'destination')
        assert test_value.get_hidde_beneficiary_account() == result


def test_get_date(date_data):
    for positive_test, result in date_data:
        test_value = Transactions(positive_test, "sender",  "description", "state", "operation_id", "sum_operation", "currency", 'destination')
        assert test_value.get_date() == result


def test_get_description_operation(data_for_operation_description):
    # positive_test = data_for_operation_description

    file = open_json('F:/PyCharm SkyP/kr_3_operations_on_accounts/tests/test.json')

    file = production_elements_operations(file)
    file = sorts_the_list_by_date(file)

    # index = 0
    for element in file:
        assert element.get_description_operation() == data_for_operation_description[0]
        assert element.get_description_operation() == data_for_operation_description[1]


# "sender", "date", "description", "state", "operation_id", "sum_operation", "currency", 'destination'