class PlayerCharacter:
    def __init__(self,name):
        self.name  = name

    def run(self):
        print('run')


player1 = PlayerCharacter('Saraj')
print(player1.name)

player1.run()

