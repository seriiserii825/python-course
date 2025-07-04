def l_10_oop_inheritance():
    class Vehicle:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def display_info(self):
            return f"Vehicle Make: {self.make}, Model: {self.model}"

    class Car(Vehicle):
        def __init__(self, make, model, num_doors):
            super().__init__(make, model)
            self.num_doors = num_doors

        def display_info(self):
            return (
                f"Car Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}"
            )
