from get_reps import get_my_reps
from Entities import *
import os

class DatabaseGateway: 

    def __init__(self):
        self.APP_PATH = os.path.dirname(os.path.abspath(__file__))
        self.issue_folder = "sample_letter/issues/"
        
        self.users = {
            "000": Person("Bob", "Builder", 
            Address("101 bob way", "bob town", "bb", "50014"),
            "bob@gmail.com")
        }
        self.users_history = {
            "000": [ParkHistoryEntry("Yellow Stone National Park", "Jan 1, 2019")]
        }
    
    def check_in_user(self, userId: str, parkName: str, date: str):
        pass
    
    def increment_advocate(self, userId: str, issueId: str):
        pass

    def get_senator_from_zip(self, zip) -> Person:

        def build_email(first, last):
            return "%s.%s@mail.house.gov"%(first, last)

        results = get_my_reps(zip)

        for result in results:
            if result[2] == "None":
                continue
            split = result[0].split(" ") # splits on name
            return Person(split[0], split[1], self.get_dummy_address(),result[2])
        
        # If we can't find anyone... just build the name (hope this is right)
        split = results[0][0].split(" ") # splits on name
        return Person(split[0], split[1], self.get_dummy_address(), build_email(split[0], split[1]))

    def get_dummy_address(self) -> Address:
        return Address("101 dummy street", "dummyville", "DA", "50014")

    def get_name_from_userId(self, userId) -> str:
        user = self.users[userId]
        return str(user)
    
    def get_email_from_userId(self, userId) -> str:
        user = self.users[userId]
        return str(user.email)
    
    def get_person_from_userId(self, userId) -> Person:
        return self.users[userId]
    
    def get_person_with_id_from_userId(self, userId) -> PersonWithId:
        return PersonWithId(self.users[userId], userId)
    
    def get_senator_from_userId(self, userId) -> Person:
        person = self.get_person_from_userId(userId)
        senator_person = self.get_senator_from_zip(person.address.zipcode)

        return senator_person
    
    def get_park_history_from_userId(self, userId):
        return self.users_history[userId]

    def get_issue_body(self, issueId) -> str:
        path = os.path.join(self.APP_PATH, self.issue_folder, "%s%s"%(issueId, ".txt"))
        with open(path) as f:
            text = f.read()
        
        return text


if __name__=="__main__":
    db = DatabaseGateway()
    sen = db.get_senator_from_zip(50014)
    print(sen.email)