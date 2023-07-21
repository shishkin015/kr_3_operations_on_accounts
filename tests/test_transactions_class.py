from utils.Transactions import Transactions


def test_gets_a_hidden_score_sender(hidden_sender_information):
    for positive_test, result in hidden_sender_information:
        test_value = Transactions("amount", 40701.91, "currency", "name", "USD", "code", "USD", positive_test)
        assert test_value.gets_a_hidden_score_sender() == result


def test_get_hidde_beneficiary_account(hidden_destination_information):
    for positive_test, result in hidden_destination_information:
        test_value = Transactions("amount", 40701.91, "currency", "name", "USD", "code", positive_test, "USD")
        assert test_value.get_hidde_beneficiary_account() == result
