import os

class Pokemon(object):
        def __init__(self, name, level):
                self.name = name
                self.level = int(level)
        def info(self):
            index = "weak" if self.level <= 20 else "fair" if self.level <= 50 else "strong"
            return "That " + self.name + " is a " + index + " Pokemon."

print("What is your pokemon'content name?")
name = input("His/Her name is ")
level = input("\nAnd his/her level is ")
print("\n\n    => " + Pokemon(name, level).info())

os.system("pause")
