#Using get_reps.py

#import file function
from get_reps import get_my_reps

# Pass in zip as parameter
reps = get_my_reps("87313")

#Returns in list format:
#	reps = [
#		["Senator1_Name","Position","Email"],
#		["Senator2_Name","Position","Email"],
#		["Representative_Name","Position","Email"]
#	]

print(reps)