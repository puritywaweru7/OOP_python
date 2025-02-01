class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
    def make_call(self, number):
        return f"Calling {number} from {self.model}..."
    
    def battery_status(self):
        return f"{self.model} has {self.battery_life} hours of battery life left."
    
#inheritance
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, heart_rate_monitor):
        super().__init__(brand, model, battery_life)
        self.heart_rate_monitor = heart_rate_monitor

    def track_steps(self, steps):
        return f"{self.model} tracked {steps} steps today!"
    
#Creating objects
phone = Smartphone("Apple", "iPhone 16", 24)
watch = Smartwatch("Samsung", "Galaxy Watch 5", 48 , True)

#Testing methods
print(phone.make_call("0712433131"))
print(phone.battery_status())
print(watch.track_steps(4000))
        