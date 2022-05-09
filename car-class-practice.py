class Car:
    def __init__(self, owner, odometer, fuel_capacity, fuel_level, mileage):
        self.owner = owner
        self.odometer = odometer
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.mileage = mileage
    

    def refuel(self, gallons):
        tank = self.fuel_level + gallons
        if tank <= self.fuel_capacity:
            return f"{(self.fuel_level + gallons) *10 /10} gallons in your tank!"
        elif tank > self.fuel_capacity:
            return f"Only {(self.fuel_capacity - self.fuel_level) *10 /10} added to your tank!"

    def get_range(self):
        max_range = (((self.fuel_level * self.mileage) *10) /10)
        return f"Only {max_range} worth of fuel left!"

    def drive(self, miles):
        miles_left = self.mileage * self.fuel_level
        if  miles < miles_left:
            self.odometer += miles
            return (f"{(self.odometer) *10 /10} miles added to the odometer!") 
        elif miles >= miles_left:
            self.odometer += miles_left
            return (f"{(miles_left) *10 /10} miles added to the odometer! OUT OF GAS")
    
def car_run(car):
    i = input("What would you like to do? Drive + miles, Refuel + gallons, Range, Exit?")
    a = i.split()
    while a[0].lower() != "exit":
        if a[0].lower() == "refuel":
            print(car.refuel(int(a[1])))
        elif a[0].lower() == "drive":
            print(car.drive(int(a[1])))
        elif a[0].lower() == "range":
            print(car.get_range())
        else:
            print("Re-enter input!")
        print(f'Odometer: {bob.odometer}')
        i = input("What would you like to do? Drive + miles, Refuel + gallons, Range, Exit?")
        a = i.split()
        
bob = Car("Bob", 0, 20, 5, 20)
car_run(bob)
