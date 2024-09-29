# def is_automorphic(num):
#     # Calculate the number of digits
#     num_of_digits = len(str(num))

#     # Compute the square of the number
#     square = num ** 2

#     # Obtain the last digits of the square
#     last_digits = square % pow(10, num_of_digits)

#     # Compare the last digits with the original number
#     return last_digits == num

# # Test the function
# num = int(input("Enter a number you want to check: \n"))

# if is_automorphic(num):
#     print("Yes, {} is an automorphic number".format(num))
# else:
#     print("No, {} is not an automorphic number".format(num))


# def automorphic(num):
#     num_of_digits=len(str(num))
#     sq=num**2
#     lt_dig=sq*pow(10,num_of_digits)
#     return lt_dig==num
# num=int(input("enter the number:"))
# if automorphic(num):
#     print("automorphic",num)
# else:
#     print(" not automorphic",num)


###############################################################

# class Animal:
#     def __init__(self,animal):
#         self.animal=animal
# class Anm(Animal):
#     def __init__(self,animal,sound):
#         super.__init__(animal)
#         self.sound=sound
#     def Animal_det(self):
#         return f"{self.animal} Sound:{self.sound}"
# aw=Anm("Cat","maww")
# print(aw.Animal_det())



# class Animal:
#     def __init__(self, animal):
#         self.animal = animal
# class Animal2(Animal):
#     def __init__(self, animal, sound): 
#         super. __init__(animal)      
#         self.sound = sound
#     def full(self):
#         return f"{self.animal} Sound: {self.sound}"
# aw = Animal2("Cat", "meow")
# print(aw.full())




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













