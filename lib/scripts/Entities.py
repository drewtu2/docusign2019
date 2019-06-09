
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
        return self.street+"\n"+self.city+self.state+self.zipcode

class ParkHistoryEntry:
    def __init__(self, park: str, date: str):
        self.park = park
        self.date = date

    def __str__(self):
        return self.park+ " on "+ self.date + "\n"

