class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sit(self):
        print(f'{self.name} is sitting')
    
    def roll_over(self):
        print(f'{self.name} is roll over')

class BlackDog(Dog):
    def __init__(self, name, age):
        super().__init__(name,age)

    
