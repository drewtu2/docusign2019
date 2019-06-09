#This file contains the tools for adding a check-in and for pulling advocacy results
from DatabaseGateway import DatabaseGateway
from location import get_nearest_park
from datetime import datetime

#For when the front-end clicks the check-in button
def save_checkin(latitude, longitude):
	db = DatabaseGateway()
	time = datetime.today().strftime('%m - %d - %Y')
	db.check_in_user('000', get_nearest_park(latitude,longitude), time)
