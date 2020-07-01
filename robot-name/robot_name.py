from random import randint
from random import sample

class Robot:

    taken_names = []

    def __init__(self):
        self.name = self.new_name()
        print('you created a new robot')


    def new_name(self):
        '''
        Generates a random name
        '''
        number_part = str(randint(100,1000))
        letters = list('ABCDEFGHIJKLMNOPQRSTUWXYZ')
        letter_part = ''.join(sample(letters, k=2))
        unique_name = letter_part + number_part
        self.taken_names.append(unique_name)

        return unique_name

    def reset(self):
        '''
        Resets robot name to a new one
        '''
        name2 = self.new_name()
        if name2 in self.taken_names:
            name2 = self.new_name()
            self.name = name2
            return self.name
        else:
            return self.name


robotos = Robot()

print(robotos.name)
robotos.reset()

print(robotos.name)
