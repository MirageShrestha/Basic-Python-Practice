# import datetime
#
# class Player:
#     def __init__(self, fname, lname, birth_year):
#         self.first_name = fname
#         self.last_name = lname
#         self.birth_year = birth_year
#
#     def get_age(self):
#         now = datetime.datetime.now()
#         return now.year - self.birth_year
#
# class CricketPlayer(Player):
#     def __init__(self, fname, lname, birth_year, team):
#         Player.__init__(self, fname, lname, birth_year)
#         self.team = team
#         self.scores = []
#
#     def add_score(self, score):
#         self.scores.append(score)
#
#     def get_average_score(self):
#         return sum(self.scores)/len(self.scores)
#
#
# class TennisPlayer(Player):
#     def __init__(self, fname, lname, birth_year, gwinner):
#         Player.__init__(self, fname, lname, birth_year)
#         self.grand_slam_winner = gwinner
#         self.aces =[]
#
#     def get_avg_aces_per_match(self):
#         return sum(self.aces)/len(self.aces)
#
# roger=TennisPlayer('roger', 'federer', 1981, 20)
# print("Age of roger federer: ", roger.get_age())
#
#
# virat = CricketPlayer('virat', 'kohli', 'india', 1988)
# virat.add_score(35)
# virat.add_score(75)
# virat.add_score(70)
#
# print('Age', virat.get_age())
# print('Average Score', virat.get_average_score())
#
#
# class BMW:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
#
#     def start(self):
#         print("Starting the car ...")
#
#     def stop(self):
#         print("Stopping the car ...")
#
#     def drive(self):
#         pass
#
#
# class ThreeClass(BMW):
#     def __init__(self, CuriseAssistEnabled, name, model, year):
#         BMW.__init__(self, name, model, year)
#         self.CuriseAssistEnabled = CuriseAssistEnabled
#
#     def display(self):
#         print(self.CuriseAssistEnabled)
#
#     def drive(self):
#         print("Three Class is being driven..")
#
#
# threeClass = ThreeClass(True, "BMW", "328i", 2018)
# threeClass.start()
# threeClass.drive()
# threeClass.stop()

class MobilePhone:

    def __init__(self, screenType, networkType, dualSim, frontCamera, camera, RAM, storage):
        self.screenType = screenType
        self.networkType = networkType
        self.dualSim = dualSim
        self.frontCamera = frontCamera
        self.camera = camera
        self.RAM = RAM
        self.storage = storage

    def make_call(self):
        pass

    def recieve_call(self):
        pass

    def take_a_picture(self):
        pass


# Let's create Apple Class
class Apple(MobilePhone):

    def __init__(self, productName, networkType, RAM, storage):
        self.productName = productName
        super().__init__(screenType='Touch Screen',
                         camera="12MP",
                         frontCamera="8MP",
                         dualSim=False,
                         networkType=networkType,
                         RAM=RAM,
                         storage=storage)

    def make_call(self):
        print(f"Making a call from {self.productName} Apple mobile phone.")

    def recieve_call(self):
        print(f"Recieving a call on {self.productName} Apple mobile phone.")

    def take_a_picture(self):
        return f"Taking Picture on {self.productName} with {self.camera} camera"

    def get_info(self):
        return f"""Product Name: {self.productName}
        Camera: {self.camera}
        Network Type: {self.networkType}
        ...
        """
        # etc

    def __str__(self) -> str:
        return f"Apple({self.productName}, {self.storage}, ...)"


# creating samsung Class
class Samsung(MobilePhone):

    def __init__(self, productName, networkType, dualSim, frontCamera, camera, RAM, storage):
        self.productName = productName
        super().__init__(screenType='Touch Screen',
                         camera=camera,
                         frontCamera=frontCamera,
                         dualSim=dualSim,
                         networkType=networkType,
                         RAM=RAM,
                         storage=storage)

    def make_call(self):
        print(f"Making a call from {self.productName} Samsung mobile phone.")

    def recieve_call(self):
        print(f"Recieving a call on {self.productName} Samsung mobile phone.")

    def take_a_picture(self):
        return f"Taking Picture on {self.productName} with {self.camera} camera"

    def get_info(self):
        return f"""Product Name: {self.productName}
        Camera: {self.camera}
        Network Type: {self.networkType}
        ...
        """
        # etc

    def __str__(self) -> str:
        return f"Samsung({self.productName}, {self.storage}, ...)"


# apple phones

apple1 = Apple("Iphone6", "4G", "4GB", "64GB")
apple2 = Apple("Iphone8", "5G", "6GB", "128GB")

# Samsung Phones

samsung1 = Samsung("Samsung1", "4G", True, "16MP", "32MP", "4GB", "64GB")
samsung2 = Samsung("Samsung2", "3G", True, "8MP", "16MP", "3GB", "16GB")

print(apple1)
apple2.make_call()
samsung1.recieve_call()
apple1.take_a_picture()
print(samsung2.get_info())
