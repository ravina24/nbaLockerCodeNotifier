#Schedule every half hour using pythonanywhere

# get json data from https://www.nba2k.io/nba-2k20-locker-codes/
# get first locker code
# compare id with previous first locker code
# if same, end execution and wait until script runs again in half hour
# if diff, send locker code to given phone numbers
# save this new locker code as previous locker code

import requests
import json

print "beginning of script"

class LockerCode:
  def __init__(self, lockerCode, expiration):
    self.lockerCode = lockerCode
    self.expiration = expiration

currentLockerCodeAmount = 124

url = "https://www.nba2k.io/page-data/nba-2k20-locker-codes/page-data.json"
response = requests.get(url)

jsonResponse = response.json()

prettyJson = json.loads(json.dumps(jsonResponse))

lockerCodesJson = prettyJson["result"]["data"]["allLockerCodes"]["edges"]

lockerCodesJsonLength = len(lockerCodesJson)

print("NUMBER OF LOCKER CODES")
print (lockerCodesJsonLength)

if lockerCodesJsonLength > currentLockerCodeAmount: #126 vs 124 -> 2
	# send text to phone numbers with locker codes, time limits (check exp date first)
	allNewLockerCodes = []
	numNewLockerCodes = lockerCodesJsonLength - currentLockerCodeAmount;
	index = 0;

	while numNewLockerCodes > 0:
		newLockerCodeJson = lockerCodesJson[index]["node"]
		newLockerCode = LockerCode(newLockerCodeJson["lockerCode"], newLockerCodeJson["expiration"])
		allNewLockerCodes.append(newLockerCode)
		index+=1
		numNewLockerCodes-=1

	#for code in allNewLockerCodes:
		#print(code.lockerCode)

	
	# set currentLockerCodeAmount ENVIRONMENT VARIABLE to lockerCodesJsonLength, increment index, decrement numNewLockerCodes
	currentLockerCodeAmount = lockerCodesJsonLength

else:
	# end script w/ no changes
	print "end of script"


#print(json.dumps(lockerCodesJson))




