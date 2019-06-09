def get_my_location(latitude, longitude):
    
	#Parameters: our current location at check-in
	#Returns: a sorted list of the causeIDs, nearest to furthest
	    
	#import requests library
	import requests

	#specify google api - geocode
	url = "https://maps.googleapis.com/maps/api/geocode/json"
	#Google cloud key
	key = "AIzaSyADl4FKdSyZFr_cIpnFSXJKctA0fqNLcGQ"

	#Parameters for get request
	params = {'key': key,
	'latlng' : str(latitude) +","+str(longitude)}

	#Sending get request and extracting data from returned JSON file
	r = requests.get(url = url, params = params)
	data = r.json()
	address = data['results'][0]['formatted_address']
	return(address)



def get_park_coordinates(park_name):
    
	#Parameters: park name
	#Returns: a tuple of latitude & longitude
	    
	#import requests library
	import requests

	#specify google api - geocode
	url = "https://maps.googleapis.com/maps/api/geocode/json"
	key = "AIzaSyADl4FKdSyZFr_cIpnFSXJKctA0fqNLcGQ"

	#Parameters for get request
	params = {'key': key,
	'address' : park_name}

	#Sending get request and extracting data from returned JSON file
	r = requests.get(url = url, params = params)
	data = r.json()
	lat = data['results'][0]['geometry']['location']['lat']
	lng = data['results'][0]['geometry']['location']['lng']
	return(lat,lng)




def get_nearest_park(latitude, longitude):
	
	#Parameters: our current location at check-in
	#Returns: a sorted list of nearby park names
	    
	#import requests library
	import requests

	#import MATHHHHHHHH
	import math

	#specify arcx api - Forest
	url = "https://apps.fs.usda.gov/arcx/rest/services/EDW/EDW_ProclaimedForestBoundaries_01/MapServer/0/query?where=1%3D1&outFields=FORESTNAME&returnGeometry=false&outSR=&f=json"

	#Sending get request and extracting data from returned JSON file
	r = requests.get(url = url)
	data = r.json()

	park_geo = []
	i=0
	while True:
		try:
			name = data['features'][i]['attributes']['FORESTNAME']
			print(name)
			lat,lng = get_park_coordinates(name)
			print(lat,lng)
			park_geo.append([name, lat, lng])
			i+=1
		except:
			('Out of Bounds, Exit')
			break

	#Get distance from our location to each park
	park_rank = []
	for park in park_geo:
		name = park[0]
		distance = (park[1]-latitude)**2 + (park[2]-longitude)**2
		distance = math.sqrt(distance)
		park_rank.append([name, distance])
	
	#Sort that list based on distance, in increasing distance
	park_rank.sort(key = lambda x: x[1])

	#Form new list with just the causeid (distance is not necessary)
	park_ranked = []
	for park in park_rank:
			park_ranked.append(park[0])

	print(park_ranked)





def get_nearest_causes(latitude, longitude):
	import math
	#Parameters: our current location at check-in
	#Returns: a sorted list of the causeIDs, nearest to furthest


	#Hardcoding the three causes and their geolocation
	cause_geo = [[1,68.1532, -151.7041], [2, 35.3874, -119.0169], [3,36.0327, -107.5729]]

	#Get distance from our location to each cause
	cause_rank = []
	for cause in cause_geo:
		causeid = cause[0]
		distance = (cause[1]-latitude)**2 + (cause[2]-longitude)**2
		distance = math.sqrt(distance)
		cause_rank.append([causeid, distance])
		    
	#Sort that list based on distance, in increasing distance
	cause_rank.sort(key = lambda x: x[1])


	#Return list of causes, sorted by ascending distance
	return cause_ranked