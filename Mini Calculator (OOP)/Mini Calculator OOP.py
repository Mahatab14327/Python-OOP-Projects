class Calculator:
    def __init__(self, brand_name):  
        self.brand = brand_name
        
    def add(self, num1, num2):
        result = num1 + num2
        return result 

    def subtract(self, num1, num2):
        result = num1 - num2
        return result

my_calc = Calculator("Casio")

print(f"Brand name: {my_calc.brand}")

print("Sum:", my_calc.add(20, 10)) 
print("Difference:", my_calc.subtract(20, 10))

print("Thanks for Using My First OOP Project Take Love From Mahatab :)(Learning OOP)")
