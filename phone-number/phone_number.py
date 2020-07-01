from string import digits

class PhoneNumber:

    def __init__(self, number):
        self.number = self.extract_digits(number)
        self.area_code = self.number[0:3]

    def extract_digits(self, number):
        number = ''.join(d for d in number if d in digits)

        if number[0]=='1':
            number = number[1:]

        if len(number) != 10:
            raise ValueError('Not a valid number.')

        if number[0] not in '23456789':
            raise ValueError('Area code must start with digit 2-9.')
        if number[3] not in '23456789':
            raise ValueError('Exchange code must start with digit 2-9.')
        return number

    def pretty(self):
        pretty_look = f'({self.area_code}) {self.number[3:6]}-{self.number[6:]}'
        return pretty_look
