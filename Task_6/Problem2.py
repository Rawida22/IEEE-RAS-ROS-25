class person:
    def __init__(self,name,country ,date_of_birth):
        self.name = name
        self.country = country
        self.date = date_of_birth

    def age (self) :
        return f"Age:{num}"  
        
person_one = person(f"Ferdi Odilia","France","1962-07-12")  
num = 60

print(f"Name:{person_one.name}")
print(f"Country:{person_one.country}")
print(f"Date of Birth:{person_one.date}")
print(person_one.age())

