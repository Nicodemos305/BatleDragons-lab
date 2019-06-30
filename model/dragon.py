class Dragon:

    def __init__(self):
        self.name = ''
        self.hp = 100
        self.atk = 15

    def status_dragon(self, name, atk, hp, race):
        print("Dragao {} selecionado".format(race))
        print("Nome {} Atk {} HP {}".format(name, atk, hp))

    def set_status(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def born_dragon(self, name, race):
        self.name = name
        if race == "1":
           self.set_status(17, 80)
           self.status_dragon(self.name, self.atk, self.hp, 'gelo')
        if race == "2":
            self.set_status(16, 90)
            self.status_dragon(self.name, self.atk, self.hp, "fogo")
        if race == "3":
           self.set_status(15, 100)
           self.status_dragon(self.name, self.atk, self.hp, "comun")
        return self