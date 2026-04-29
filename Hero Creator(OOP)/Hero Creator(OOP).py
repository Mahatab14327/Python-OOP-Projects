class Hero:
    def __init__(self,name,role,level=1):
        self.name = name
        self.role = role
        self.level = level
    def introduce(self):
     print(f"\n--- Character Created! ---")
     print(f"Welcome {self.name} the {self.role}!")
     print(f"Your starting level is {self.level}")
    
print("Welcome to the Adventure lobby")

user_name = input("Enter your Hero's name:")
user_role = input("Choose a Role (Warrior/Mage/Archer):")

my_hero = Hero(user_name,user_role)

my_hero.introduce()
print("Thanks for creating your hero! Enjoy your adventure! Take love from Mahatab :)")