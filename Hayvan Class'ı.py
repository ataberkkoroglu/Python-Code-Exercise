from msilib.schema import Condition
from turtle import delay


class Animal():
    def __init__(Self,name,gender,age,number_of_foot,weight,height,race):
     Self.name=name
     Self.gender= gender
     Self.age= age
     Self.number_of_foot = number_of_foot
     Self.weight= weight
     Self.height= height
     Self.race= race
    def __str__(Self):
      
      print("Be Showing Informations")
      delay(5)
      print("Name:{} \nGender:{} \nAge:{} \nNumber Of Foot:{} \nWeight:{} \nHeight:{} \nRace:{} ".format(Self.name,Self.gender,Self.age,Self.number_of_foot,Self.weight,Self.height,Self.race))

class dog(Animal):
    def __init__(Self,name,Gender,Age,Number_of_Foot,Weight,Height,Race):
     print("your giving informations is relevant Dog...")
     super().__init__ (name,Gender,Age,Number_of_Foot,Weight,Height,Race)
     

class bird(Animal):
    def __init__(Self,name,Gender,Age,Number_of_Foot,Weight,Height,Race):
     print("your giving informations is relevant Bird...")
     super().__init__(name,Gender,Age,Number_of_Foot,Weight,Height,Race)


class horse(Animal):
    def __init__(Self,name,Gender,Age,Number_of_Foot,Weight,Height,Race):
     print("your giving informations is relevant Horse...")
     super().__init__(name,Gender,Age,Number_of_Foot,Weight,Height,Race)

Badem= dog("Badem","Female",6,4,10,2,"Smokin")
Badem.__str__()

