class Vehicle:
    def move(self):
        pass #abstract method
class Car(Vehicle):
    def move(self):
        return "Driving on the road!"
    
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky!!"
    
class Boat(Vehicle):
    def move(self):
        return "Sailing in the water!!"
    
#Testing using array called vehicles 
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())