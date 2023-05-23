
import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_study(self):
        print("Time to study")
        self.progress +=0.12
        self.gladness -= 3


    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness +=5
        self.progress -= 0.1
        pass
    def is_alive(self):
        if self.progress < -0.5:
           print("Cast out...")
           self.alive = False

        elif self.gladness <=0:
            print("Depresson...0")
            self.alive = False

        elif self.progress > 5:
            print("Passed e[ternally...")
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress,2)}')

    def live(self,day):
         day = "Day" + str(day) + "of" + self.name + "life"
         print (f'{day:=^50})')
         print('1 - for study')
         print('2 - for sleep')
         print('3 - for chill')
         live_cube = (input('Enter your choice:'))
         if  live_cube == '1':
            print('You entered 1 variant (study)')
            self.to_study()

         elif live_cube == "2":
            print('You entered 2 variant (sleep)')
            self.to_sleep()

         elif  live_cube == "3":
            print('You entered 3 variant (chill)')
            self.to_chill()
         else:
            print("! Not correct choice")
         self.end_of_day()
         self.is_alive()

         def __init__(self, name,mony):
             self.name = name
             self.gladness = 50
             self.progress = 0
             self.alive = True

         def to_study(self):
             print("Time to study")
             self.progress += 0.12
             self.gladness -= 3

         def to_sleep(self):
             print('I will sleep')
             self.gladness += 3

         def to_chill(self):
             print("Rest time")
             self.gladness += 5
             self.progress -= 0.1

         def is_alive(self):
             if self.progress < -0.5:
                 print("Cast out...")
                 self.alive = False
             elif self.gladness <= 0:
                 print("Depression...0")
                 self.alive = False
             elif self.progress > 5:
                 print("Passed eternally...")
                 self.alive = False

         def random_event(self):
             event = random.randint(1, 3)
             if event == 1:
                 print("You caught a cold!")
                 self.gladness -= 5
             elif event == 2:
                 print("You received a surprise gift!")
                 self.gladness += 5
             elif event == 3:
                 print("You found a great study resource!")
                 self.progress += 0.5

         def work(self):
             print("Time to work")
             earnings = random.randint(5, 20)  # Случайно генерируем заработок
             self.money += earnings
             self.gladness -= 2
             self.progress += 0.1

         def end_of_day(self):
             print(f'Gladness = {self.gladness}')
             print(f'Progress = {round(self.progress, 2)}')
             print(f'Money = {self.money}')

nick=Student(name='Nick')
for day in range(365):
    if nick.alive==False:
       print("Student Lose")
       break
    nick.live(day)


