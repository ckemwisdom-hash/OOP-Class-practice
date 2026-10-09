# Object Oriented programming - 1 (OOP-1)

class animal:
    def __init__(self, name):
        self.name = name

        def speak(self):
            print(f"{self.name} makes a sound")
class Dog(animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(animal):
            def speak(self):
                print(f"{self.name} meows")
                for animal in [Dog("rex"), Cat ("milo")]:
                    animal.speak()
# Person Class
class Person:
    def __init__(self, name, age,gender, person_id, height, program):
     self.name = name
     self.age = age
     self.gender = gender
     self.person_id = person_id
     self.height = height
     self.program = program

    def print_bio(self):
        print("printing person details")
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.gender}")
        print(f"{self.person_id}")
        print(f"{self.height}")
        print(f"{self.program}")
        print("========================================")

# Person object
person1 = Person("Kem", 19, "Male", 4997, 6.0, "BSEM")
person2 = Person("boyce", 45, "Male", 4987, 6.5, "BICT")
person3 = Person("Michael", 34, "Male", 5678, 5.7, "BBIT")


person1.print_bio()
person2.print_bio()
person3.print_bio()
