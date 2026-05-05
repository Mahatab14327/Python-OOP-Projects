class SmartWatch:
    def __init__(self, brand):
        self.brand = brand
        self.steps = 0
    def walk(self, amount):
      if amount > 0:
        self.steps += amount
        print(f"{self.brand} SmartWatch: You walked {amount} steps. Total steps: {self.steps}")
      else:
        print("Please enter a positive number of steps.")
    def     reset_steps(self):
        self.steps = 0
        print(f"{self.brand} SmartWatch: Steps have been reset. Total steps: {self.steps}")

                            ###Main program###

    print("Welcome to the Steps Tracker!")
watch_name = input("Enter the brand of your SmartWatch: ")
my_watch = SmartWatch(watch_name)

distance = int(input("Enter the number of steps you walked: "))
my_watch.walk(distance)

dist2 = int(input("Walked some more? Enter steps: "))
my_watch.walk(dist2)