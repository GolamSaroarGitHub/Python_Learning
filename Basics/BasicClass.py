class Enemy:
    life=10
    def attack(self):
        print('ouch!!')
        self.life=self.life-1

    def checklife(self):
        print(str(self.life)+ ' life left' )

enemy1=Enemy()
enemy2=Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()