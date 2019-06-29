class Dragon:

    def __init__(self):
        self.name = ''
        self.hp = 100
        self.atk = 15

    def born_dragon(self, name, race):
        self.name = name
        if race == "1":
           self.atk = 17
           self.hp = 80
           print("Dragao de gelo selecionado")
        if race == "2":
            self.atk = 16
            self.hp =90
            print("Dragao de fogo selecionado")
        if race == "3":
           self.atk = 15
           self.hp = 100
           print("Dragao comun selecionado")
        return self

