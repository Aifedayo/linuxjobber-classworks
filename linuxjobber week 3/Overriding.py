# Overriding Methods

class Robot:
    def __init__(self):
        pass

    def Action(self):
        print('I am Will Smith from the Future')

class Human(Robot):
    def __init__(self):
        super().__init__()
        
    def Action(self):
        print('I would not make human actions obsolete')

c = Human()
c.Action()
