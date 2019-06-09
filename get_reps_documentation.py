#Using get_reps.py

#import file function
from get_reps import get_my_reps

# Pass in address as parameter
reps = get_my_reps("44 Tehama St, San Francisco, CA 94105")

#Returns in list format:
#	reps = [
#		["Senator1_Name","Position","Email"],
#		["Senator2_Name","Position","Email"],
#		["Representative_Name","Position","Email"]
#	]

print(reps)