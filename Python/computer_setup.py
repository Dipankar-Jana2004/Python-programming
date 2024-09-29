class ComputerSetup:
    def __init__(self, cp_brand, cp_model):
        self.cp_brand = cp_brand
        self.cp_model = cp_model

class Comp(ComputerSetup):
    def __init__(self, cp_brand, cp_model, mouse_brand, mouse_model, cpu_brand, cpu_model):
        super().__init__(cp_brand, cp_model)
        self.mouse_brand = mouse_brand
        self.mouse_model = mouse_model
        self.cpu_brand = cpu_brand
        self.cpu_model = cpu_model

    def full_setup(self):
        return (
            f"Output:\n"
            f"Brand: {self.cp_brand}, Model: {self.cp_model}\n"
            f"Input:\n"
            f"Mouse Brand: {self.mouse_brand}, Model: {self.mouse_model}\n"
            f"CPU Brand: {self.cpu_brand}, Model: {self.cpu_model}"
        )
my_comp = Comp("LG","Monitor","HP", "Mouse", "Intel", "i5")
print(my_comp.full_setup())