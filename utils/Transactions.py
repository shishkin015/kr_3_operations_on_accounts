from datetime import datetime


class Transactions:

    def __init__(self,
                 date: str,
                 description: str,
                 state: str,
                 operation_id: int,
                 sum_operation: float,
                 currency: str,
                 destination: str,
                 sender: str
                 ):
        self.date = date
        self.description = description
        self.state = state
        self.operation_id = operation_id
        self.sum_operation = sum_operation
        self.currency = currency
        self.destination = destination
        self.sender = sender

    def get_date(self) -> str:
        """
        Функция возвращает дату формата ДД.ММ.ГГГ
        """

        the_date = datetime.fromisoformat(self.date)
        date = the_date.strftime('%d.%m.%Y')

        return date

    def gets_a_hidden_score_sender(self) -> str:
        """
        Функция выводит информацию о карте и скрывает часть номера карты отправителя
        """
        # Номер карты замаскирован и не отображается целиком в формате MasterCard XXXX XX** **** XXXX 
        string = self.sender

        info_hidden_number = string.split(' ')

        string_list = string.split()[-1]
        star = len(string_list) - 10
        card_number = string_list[:6] + star * "*" + string_list[-4:]
        card_number = [card_number[i:i + 4] for i in range(0, len(card_number), 4)]
        card_number = " ".join(card_number)

        # Заменяем последний индекс на замаскированный номер карты
        info_hidden_number[-1] = "".join(card_number)

        return " ".join(info_hidden_number)

    def get_hidde_beneficiary_account(self) -> str:
        """
        Функция выводит счет, скрывает часть номера счета получателя
        """
        # Номер счета замаскирован и не отображается целиком в формате **XXXX
        account_number = self.destination

        hidden_beneficiary_account = account_number.split(' ')

        hidden_account = account_number.split(' ')[-1]
        hidden_account = '**' + hidden_account[-4:]

        # Заменяем последний индекс на замаскированный номер счета получателя
        hidden_beneficiary_account[-1] = "".join(hidden_account)

        return " ".join(hidden_beneficiary_account)

    def get_description_operation(self) -> str:
        """
        Функция выводит описание операции
        """
        # <дата перевода> <описание перевода>
        line_output = f"{self.get_date()} {self.description}\n"

        # <откуда> -> <куда> 
        if self.sender is not None:
            line_output += f"{self.gets_a_hidden_score_sender()} -> {self.get_hidde_beneficiary_account()}\n"
        else:
            line_output += f"{self.get_hidde_beneficiary_account()}\n"

        # <сумма перевода> <валюта>
        line_output += f"{self.sum_operation} {self.currency}\n"

        return line_output
