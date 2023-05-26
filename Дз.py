import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 0

    def __str__(self):
        return f"Cat: {self.name} (Hunger: {self.hunger}, Energy: {self.energy})"

    def play(self):
        self.energy -= 1
        print(f"{self.name} is playing.")
        self._check_energy()

    def sleep(self):
        self.energy += 2
        print(f"{self.name} is sleeping.")
        self._check_energy()

    def eat(self):
        self.hunger -= 2
        print(f"{self.name} is eating.")
        self._check_hunger()

    def _check_energy(self):
        if self.energy < 0:
            print(f"{self.name} is exhausted.")
            self.energy = 0
        elif self.energy > 10:
            print(f"{self.name} is hyperactive.")
            self.energy = 10

    def _check_hunger(self):
        if self.hunger < 0:
            print(f"{self.name} is full.")
            self.hunger = 0
        elif self.hunger > 10:
            print(f"{self.name} is hungry.")
            self.hunger = 10

    def simulate(self, time_steps):
        for _ in range(time_steps):
            action = random.choice(["play", "sleep", "eat"])
            if action == "play":
                self.play()
            elif action == "sleep":
                self.sleep()
            elif action == "eat":
                self.eat()
            print(self)


# Приклад використання:
cat = Cat("Whiskers")
cat.simulate(5)