# class fruit:
#     def __init__(self):
#         self.name = "avacado"
#         self.colour = "green"
# my_fruit = fruit()
# print(my_fruit.name)
# print(my_fruit.colour)


# class fruit:
#     def __init__(self, name, clr):
#         self.name = name
#         self.colour = clr
#     def details(self):
#         print("my " + self.name + " is " + self.colour)
        
# apple = fruit("apple", "red")
# apple.details()        


# class animal:
#     def __init__(self, animal_a, animal_b):
#         self.animal1 = animal_a
#         self.animal2 = animal_b
        
#     def details(self):
#         print("I had " , self.animal1, " and " , self.animal2 )

# pets = animal("dog", "cat")
# pets.details()

# class person:
#     def __init__(self, ramesh, suresh):
#         self.traveler = ramesh
#         self.driver = suresh
        
#     def details(self):
#         print(self.traveler , " is going to goa with driver ", self.driver )
# tourist  = person("ramesh", "suresh")
# tourist.details()

# class animal:
#     def __init__(self, animal_a, animal_b):
#         self.animal1 = animal_a  
#         self.animal2 = animal_b  
        
#     def details(self):
#         print("I had", self.animal1, "and", self.animal2)
# anmls = animal("dog", "cat")
# anmls.details()


# class named_animals(animal):
#     def __init__(self, Barn, Roxy): 
#         super().__init__("dog", "cat")  
#         self.dog_name = Barn         
#         self.cat_name = Roxy        
        
#     def details(self):  
#         print("I have a" , self.animal1, "named" , self.dog_name, "and a", self.animal2 , "named" ,self.cat_name)


# pets = named_animals("Barn" , "Roxy")
# pets.details()  



class person:
    def __init__(self):
        self.name = "jaunty"
        self.age = 23
my_details = person()
print(my_details.name)
print(my_details.age)