class Person:
    count_instances = 0
    
    def __init__(self, name, age):
        Person.count_instances+=1
        self.name = name 
        self.age = age 
    
    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count_instances} instance in {cls.__name__} class"

    def full_name(self):
        return f"The full name of the candidate is {self.name}"

    def is_above_18(self):
        return self.age<18

P1 = Person("Indranil",24)
P2 = Person("xyz",19)
print(Person.count_instance())
