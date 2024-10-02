# 9.1 Classes and Objects

# Classes make objects.
# The are like a blueprint to make something

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print(f"{self.name} says, \"Woof.\"")

    def fetch(self, object):
        print(f"You threw a(n) {object}")
        print(f"{self.name} retrieved the {object}")


luna = Dog("Luna", "Lab")

dave = Dog("Dave", "Pitt-Greyhound mix")

print(luna.name)
print(luna.breed)
print(dave.breed)

# Changing values in an object
dave.name = "Collin"
print(dave.name)

luna.speak()

luna.fetch("ball")
dave.fetch("stick")