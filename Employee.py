import requests


class Employee:
    raise_amt = 1.05

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'.lower()

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    # example of "mocking"
    def montly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
