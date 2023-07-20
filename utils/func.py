# <дата перевода> <описание перевода>
# <откуда> -> <куда>
# <сумма перевода> <валюта>
from utils.py_dict import Element


class Transaction(Element):
    def date_output_description(self):
        print(f'{self.date} {self.description}')
