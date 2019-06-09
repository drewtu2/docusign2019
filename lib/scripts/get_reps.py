def get_my_reps(address):
	#import requests library
	import requests

	# Get request:
	# GET https://www.googleapis.com/civicinfo/v2/representatives

	url = "https://www.googleapis.com/civicinfo/v2/representatives"

	key = "AIzaSyADl4FKdSyZFr_cIpnFSXJKctA0fqNLcGQ"

	# address = "1107 High School Way, FRNT, Mountain View, California, 94041"
	params = {'key': key,
	'address' : address,
	'levels' : 'country'}
	
	r = requests.get(url = url, params = params)

	data = r.json()
	officials = data['officials']

	return_data = []
	return_len = len(officials)
	for i in range(2,5):
	    name = data['officials'][i]['name']
	    
	    if i == 2 or i == 3:
	        position = 'Senator'
	    else:
	        position = 'Representative'
	        
	    try:
	        email = data['officials'][i]['emails'][0]
	    except:
	        email = 'None'

	    print(name, position, email)

	    
	    return_data.append([name,position, email])
	return return_data


#Arbitrary Trump Pic:
trump_pic = "https://www.whitehouse.gov/sites/whitehouse.gov/files/images/45/PE%20Color.jpg"
