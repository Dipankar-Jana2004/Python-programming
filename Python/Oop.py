# class Family:
#     def _init_(self, First_person, Second_person, Third_person):
#         self.First_person = First_person
#         self.Second_person = Second_person
#         self.Third_person = Third_person

# class Family2(Family):
#     def _init_(self, First_person, Second_person, Third_person, Fourth_person):
#         super()._init_(First_person, Second_person, Third_person)  
#         self.Fourth_person = Fourth_person
    
#     def fullfamily(self):
#         return f"{self.First_person}, {self.Second_person}, {self.Third_person}, {self.Fourth_person}"

# fam = Family2("Dip", "Avi", "Tuhin", "Gopal")
# print(fam.fullfamily())

# class Computer_setup:
#     def __init__(self,cp_brand,cp_model):
#         self.cp_brand=cp_brand
#         self.cp_model=cp_model
# class Comp(Computer_setup):
#     def __init__(self, cp_brand, cp_model, CPU):
#         super().__init__(cp_brand, cp_model)
#         self.CPU=CPU
#     def full_setup(self):
#         return f"Output:{self.cp_brand} Input{self.cp_model} CPU{self.CPU}"
# my_comp=Comp("Monitor","LG", "mouse","Hp","Intel")
# print(my_comp.full_setup())


