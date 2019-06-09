
class Profile():
    def __init__(self, id, person, history):
        self.id = id
        self.person = person
        self.history = history

class PersonWithId():
    def __init__(self, person, id):
        self.id = id
        self.person = person
    
    def __str__(self):
        return self.person.first + " " + self.person.last
        


class Person:
    def __init__(self, first, last, address, email):
        self.first = first
        self.last = last
        self.address = address
        self.email = email
    
    def __str__(self):
        return self.first + " " + self.last
        


class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        return "%s\n%s, %s %s" % (self.street, self.city, self.state, str(self.zipcode))

class ParkHistoryEntry:
    def __init__(self, park: str, date: str):
        self.park = park
        self.date = date

    def __str__(self):
        return self.park+ " on "+ self.date + "\n"

