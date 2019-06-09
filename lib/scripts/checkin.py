#This file contains the tools for adding a check-in and for pulling advocacy results
from DatabaseGateway import DatabaseGateway
from location import get_nearest_park
from datetime import datetime
import argparse

#For when the front-end clicks the check-in button
def save_checkin(latitude, longitude):
	db = DatabaseGateway()
	time = datetime.today().strftime('%m - %d - %Y')
	output = get_nearest_park(latitude,longitude)
	print(output)
	db.check_in_user('000', output, time)

if __name__ == "__main__":
    parser=argparse.ArgumentParser()

    parser.add_argument('--lat', type=float, help='Lat')
    parser.add_argument('--long', type=float, help='Long')
    args=parser.parse_args()
    
    print(save_checkin(args.lat, args.long))
