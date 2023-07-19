from datetime import datetime
class Element:
    def __init__(self, list_of_operations):
        self.list_of_operations = list_of_operations

        self.last_five_details = detailes[-5:]
        self.to = None
        self.from_ = None
        self.description = None
        self.operationAmount = None
        self.state = None
        self.id = None
        self.date = None
        self.operation = None

    def get_details(self):
        details = []
        for operations in self.list_of_operations:
            if operations['state'] == 'EXECUTED':
                details.append(operations['state'])

            
    def get_id(self):
        self.id = self.last_five_details["id"]

    def get_date(self):
        date = self.last_five_details["date"]
        self.date = datetime.fromisoformat(date)

    def get_state (self):
        self.state = self.last_five_details["state"]

    def get_operationAmount(self):
        self.operationAmount = self.last_five_details["operationAmount"]

    def get_description (self):
        self.description = sself.last_five_details["description"]

    def get_from(self):
        self.from_ = self.last_five_details["from"]

    def get_to(self):
        self.to = self.last_five_details["to"]