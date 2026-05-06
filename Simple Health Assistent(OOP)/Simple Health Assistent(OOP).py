class HealthAssistent:
  def   __init__(self, name):
    self.name = name
  
  def remind(self):
    print(f"\n--- Get Well Soon, {self.name}! ---")
    print("1.Drink a glass of water")
    print("2.Take your medicine on time")
    print("3.Get enough rest")
    print("4.Eat healthy food")
    print("5.Avoid stress")
    print("6.Consult a doctor if symptoms persist")
    print("Thanks for using Simple Health Assistant. Take love from Mahatab :)!")
          
name_input = input("Please enter your name: ")
user = HealthAssistent(name_input)
user.remind()
