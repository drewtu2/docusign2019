from get_reps import get_my_reps
from Entities import *
import os
import pickle

class DatabaseGateway: 

    def __init__(self):
        self.APP_PATH = os.path.dirname(os.path.abspath(__file__))
        self.issue_folder = "sample_letter/issues/"
        self.advocate_count_folder = "db/advocate_counts"
        self.users_folder = "db/users"
        
        self.users = {
            "000": Person("Bob", "Builder", 
            Address("101 bob way", "bob town", "bb", "50014"),
            "bob@gmail.com")
        }
        self.users_history = {
            "000": [ParkHistoryEntry("Yellow Stone National Park", "Jan 1, 2019")]
        }

        self._updateUser("000")
    
    def setup_users(self):
        self.register_user("000", Person("Bob", "Builder", 
            Address("101 bob way", "bob town", "bb", "50014"),
            "bob@gmail.com"))
        self.check_in_user("000", "Yellow Stone National Park", "Jan 1, 2019")
        self.check_in_user("000", "Yosemite National Park", "Feb 1, 2019")
        self.check_in_user("000", "Lassen National Park", "March 1, 2019")
        self.check_in_user("000", "Joshua Tree Park", "April 1, 2019")
    
    def register_user(self, userId: str, person: Person):
        obj = Profile(userId, person, [])

        with open(os.path.join(self.APP_PATH, self.users_folder, "%s.txt"%userId), "wb") as f:
            pickle.dump(obj, f)

    
    def check_in_user(self, userId: str, parkName: str, date: str):

        with open(os.path.join(self.APP_PATH, self.users_folder, "%s.txt"%userId), "rb") as f:
            data = pickle.load(f)
            data.history.append(ParkHistoryEntry(parkName, date))
        with open(os.path.join(self.APP_PATH, self.users_folder, "%s.txt"%userId), "wb") as f:
            pickle.dump(data, f)
        self._updateUser(userId)

    def increment_advocate(self, issueId: str):
        with open(os.path.join(self.APP_PATH, self.advocate_count_folder, "issue%s.txt"%issueId), "r") as f:
            for line in f:
                count = int(line)
                print(count)
                count +=1
                print(count)
        with open(os.path.join(self.APP_PATH, self.advocate_count_folder, "issue%s.txt"%issueId), 'w+') as f:
            f.write(str(count))
    
    def get_num_advocates(self, issueId: str):
        with open(os.path.join(self.APP_PATH, self.advocate_count_folder, "issue%s.txt"%issueId)) as f:
            for line in f:
                num_advocates = int(line)
        return num_advocates

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
    
    def _updateUser(self, userId):
        with open(os.path.join(self.APP_PATH, self.users_folder, "%s.txt"%userId), "rb") as f:
            obj = pickle.load(f)
            self.users[userId] = obj.person
            self.users_history[userId] = obj.history

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
    
    db.setup_users()
    print("history: " + str(db.get_park_history_from_userId("000")))
    db.check_in_user("000", "test", "today")
    print("history: " + str(db.get_park_history_from_userId("000")))