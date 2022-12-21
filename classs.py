class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti

    def method(self):
        print(f'hero name: {self.name}\n'
              f'hero abyliti: {self.abyliti} ')

class Hero_super(Hero):
    def __init__(self, name, abyliti):
        super().__init__(name, abyliti)

    def nick(self):
        print(f'hero name: {self.name}')

    def __str__(self):
        return f'abyliti: {self.abyliti}'

    def phrase(self):
        print('it is super_hero')




