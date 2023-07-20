from datetime import datetime

from utils.arrs_json import Operation


class Transactions:

    def __init__(self,
                 date: str,
                 description: str,
                 state: str,
                 operation_id: int,
                 sum_operation: float,
                 currency: str,
                 destination:str):
        self.date = date
        self.description = description
        self.state = state
        self.operation_id = operation_id
        self.sum_operation = sum_operation
        self.currency = currency
        self.destination = destination

    def get_date(self) -> None:
        """Функция возвращает дату формата ДД.ММ.ГГГ"""
        the_date = datetime.fromisoformat(self.date)
        date = the_date.strftime('%d.%m.%Y')
        return date

    def get_description(self) -> None:
        line_output = f"{self.date()} {self.description}\n"


    def get_operationAmount(self) -> None:
        """Сумма операции"""
        self.returns_executed("operationAmount")("amount")

    def transaction_currency(self) -> None:
        """Валюта операции"""
        self.returns_executed("operationAmount")("currency")("name")

    def get_description(self) -> None:
        """Описание операции"""
        self.returns_executed("description")

    def get_from(self) -> None:
        """От кого или от куда"""
        self.returns_executed("from")

    def get_to(self) -> None:
        """Куда или кому"""
        self.returns_executed("to")
