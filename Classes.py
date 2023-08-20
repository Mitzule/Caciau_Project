class Animal:

    def __init__(self, name):
        self.name=name
        self.air=100
        self.HO=500

    def get_stats(self):
        print(f"instance of Animal {self.name} with stats: air:{self.air} HP:{self.HP}")

    def breath(self):
        print("Air in")
        self.air+=10
        print("Air out")

    def eat(self, type_of_food=None):
        print(f"Dog ate food type {type_of_food}")

        if type_of_food==1:
            self.HP+=50
        elif type_of_food==2:
            self.HP+=50

    def __del__(self):
        print(f"__del__ initialized for {self.name} ")

if __name__=="__main__":

    Billy=Animal("Billy")

    print()
    Billy.eat(1)

    print()
    Billy.get_stats()

    print()
    Bob=Animal("Bob")

    Bob.get_stats()

    print("\n\n\n\n\n\n\n\n")

    print("Aici se executa main-ul")





