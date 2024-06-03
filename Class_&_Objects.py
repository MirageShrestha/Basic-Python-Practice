'''CLASS AND OBJECTS'''

# import datetime
# class CricketPlayer:
#     def __init__(self, fname, lname, team, b_year):
#         self.first_name = fname
#         self.last_name = lname
#         self.team = team
#         self.birth_year = b_year
#         self.scores=[]
#
#     def get_age(self):
#         now = datetime.datetime.now()
#         return now.year - self.birth_year
#
#     def add_score(self, score):
#         self.scores.append(score)
#
#     def get_average(self):
#         return sum(self.scores)/len(self.scores)
#
#     def __lt__(self, other):
#         my_score = self.get_average()
#         other_score = other.get_average()
#         return my_score < other_score
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} is a cricket player form {self.team}'
#
#
# virat = CricketPlayer('virat', 'Kohli', 'india', 1988)
# virat.add_score(80)
# virat.add_score(100)
# virat.add_score(120)
# virat.add_score(0)
# virat.add_score(10)
#
# david = CricketPlayer('david', 'warner', 'australia', 1985)
# david.add_score(87)
# david.add_score(180)
# david.add_score(10)
# david.add_score(20)
# david.add_score(19)
#
# print(virat.first_name)
# print(virat.team)
# print(virat.get_age())
# print(virat.get_average())
#
# print(david.first_name)
# print(david.team)
# print(david.get_average())
# print(david.get_age())
#
# print(virat<david)
#
# print(virat)
# print(david)

'''OPERATOR OVERLOADING'''
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __str__(self):
#         return f'Radius of circle is {self.radius}'
#
#     def __add__(self, other):
#         return Circle(self.radius + other.radius)
#
# c1 = Circle(3)
# c2 = Circle(7)
# c3 = c1 + c2
#
# print(c3)
#
# print(c1)
# print(c2)
#
# print(str(c1))
# print(format(c2))

# Python program to overload assignment operator
# class Coordinates:
#     def __init__(self,a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return "({0},{1})".format(self.a,self.b)
#
#     def __iadd__(self, other):
#         self.a += other.a
#         self.b += other.b
#         return Coordinates(self.a,self.b)
#
# obj1 = Coordinates(5,10)
# obj2 = Coordinates(2,5)
# obj2 += obj1
# print(obj2)

# class car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.speed = 70
#
#     def accelerate(self):
#         self.speed += 10
#
#     def put_brake(self):
#         self.speed -= 10
#
# tesla_model_3 = car('tesla', 3, 'white')
#
# print(tesla_model_3.put_brake())

# class Avenger:
#     def __init__(self, name, age, gender, superpower, weapon):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.superpower = superpower
#         self.weapon = weapon
#
#     def get_info(self):
#         return f'Name:{self.name} \nage:{self.age} \ngender:{self.gender} \nPower:{self.superpower} \nweapon:{self.weapon} \n'
#
#     def is_leader(self):
#         if self.name == 'Captain America':
#             return 'Leader'
#         else:
#             return 'Not a leader'
#
#
# Captain_America = Avenger('Captain America', 75, 'M', 'Superstrength', 'shield')
# Ironman = Avenger('Tony Stark', 45, 'M', 'Technology', 'Armor')
# Black_Widow = Avenger('Black Widow', 35, 'F', 'superhuman','Batons', )
# Hulk = Avenger('Hulk', 69, 'M', 'Unlimited strength', None)
# Thor = Avenger('Thor', 1200, 'M', 'Super energy', ' Mjölnir')
# Hawkeye = Avenger('Hawkeye', 38, 'M', 'fighting skills', 'bows and arrows')
#
#
# print(Captain_America.get_info())
# print(Ironman.get_info())
# print(Black_Widow.get_info())
# print(Hulk.get_info())
# print(Thor.get_info())
# print(Hawkeye.get_info())
#
# print(Captain_America.is_leader())
# print(Black_Widow.is_leader())

# creating the Avenger class

class Avenger:
    """Class to represent an Avenger"""

    def __init__(self, name, age, gender, superPower, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superPower = superPower
        self.weapon = weapon

        # is Leader
        self.isLeader = False

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_superpower(self):
        return self.superPower

    def get_info(self):
        return f"""
        Avenger Profile:

        Name:   {self.name}
        Age:    {self.age}
        Gender: {self.gender}

        Has {self.weapon} weapon and {self.superPower} super Power. 
        """
# is leader function
    def is_leader(self):
        return self.isLeader

    def make_leader(self):
        self.isLeader = True
        return f"{self.name} is the new leader of the Avengers"

    def remove_leader(self):
        self.isLeader = False
        return f"{self.name} is removed from the leader"

    def __str__(self):
        return f"Avenger({self.name}, {self.age}, ...)"

Super_heroes = ['Captain America', 'Iron Man', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
super_powers = ['Super strength', 'Technology', 'superhuman', 'Unlimited Strength', 'super Energy', 'fighting skills'] # from question
weapons = ["Shield", "Armor", "Batons", "No Weapon", "Mjölnir", "Bow and Arrows"]    #from question

# let's create a ages and gender list randomly
ages = [110, 40, 35, 34, 10000, 30]
genders = ['M', 'M', 'F', 'M', 'M', 'M']

# now create our avengers team using the data
avengers = []
for name, age, gender, power, weapon in zip(Super_heroes, ages, genders, super_powers, weapons):
    avengers.append(
        Avenger(name, age, gender, power, weapon)
    )

print(avengers[0])
avengers[0].make_leader()
# print information
print(avengers[2].get_info())
print(avengers[1].is_leader())


for avenger in avengers:
    if avenger.get_name() == 'Iron Man':
        print(avenger.get_info())

avengers[5].get_superpower()