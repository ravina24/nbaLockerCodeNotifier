#Schedule every half hour

# get json data from https://www.nba2k.io/nba-2k20-locker-codes/
# get first locker code
# compare id with previous first locker code
# if same, end execution and wait until script runs again in half hour
# if diff, send locker code to given phone numbers
# save this new locker code as previous locker code

import requests
import json
import math

print "beginning of script"
currentLockerCodeAmount = 124

url = "https://www.nba2k.io/page-data/nba-2k20-locker-codes/page-data.json"
response = requests.get(url)

jsonResponse = response.json()

prettyJson = json.loads(json.dumps(jsonResponse))

lockerCodesJson = prettyJson["result"]["data"]["allLockerCodes"]["edges"]

lockerCodesJsonLength = len(lockerCodesJson)

print("NUMBER OF LOCKER CODES")
print (lockerCodesJsonLength)

if lockerCodesJsonLength > currentLockerCodeAmount:
	# set currentLockerCodeAmount to lockerCodesJsonLength
	# send text to phone numbers with locker codes, time limits (check exp date first)
else:
	# end script w/ no changes


#print(json.dumps(lockerCodesJson))




