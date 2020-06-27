import requests
import json
from twilio.rest import Client
from datetime import datetime
from creds import (account_sid, auth_token, my_phone_numbers, my_twilio_number)


class LockerCode:
  def __init__(self, lockerCode, expiration):
    self.lockerCode = lockerCode
    self.expiration = expiration


def getNewLockerCodes():
	totalNumLockerCodesFile = open("totalNumLockerCodes.txt","r+")
	currentLockerCodeAmount = int(totalNumLockerCodesFile.read())

	url = "https://www.nba2k.io/page-data/nba-2k20-locker-codes/page-data.json"
	response = requests.get(url)

	jsonResponse = response.json()
	prettyJson = json.loads(json.dumps(jsonResponse))
	lockerCodesJson = prettyJson["result"]["data"]["allLockerCodes"]["edges"]
	lockerCodesJsonLength = len(lockerCodesJson)

	if lockerCodesJsonLength > currentLockerCodeAmount:
		allNewLockerCodes = []
		numNewLockerCodes = lockerCodesJsonLength - currentLockerCodeAmount;
		index = 0;

		while numNewLockerCodes > 0:
			newLockerCodeJson = lockerCodesJson[index]["node"]
			newLockerCode = LockerCode(newLockerCodeJson["lockerCode"], newLockerCodeJson["expiration"])
			# if newLockerCode.expiration > datetime.now(): DONT INCLUDE LOCKER CODES THAT HAVE ALREADY EXPIRED
			allNewLockerCodes.append(newLockerCode)
			index+=1
			numNewLockerCodes-=1

		
		totalNumLockerCodesFile.truncate(0)
		totalNumLockerCodesFile.seek(0)
		totalNumLockerCodesFile.write(str(lockerCodesJsonLength))
		totalNumLockerCodesFile.close()

		return allNewLockerCodes

	else:
		return []


def createText(lockerCodeArray):
	text = "New locker codes available: \n"

	for code in lockerCodeArray:
		text += code.lockerCode + " expires " + code.expiration + "\n \n"

	return text



def send_lockercode_sms():

    client = Client(account_sid, auth_token)
    newLockerCodes = getNewLockerCodes()

    if len(newLockerCodes) != 0:
    	text = createText(newLockerCodes)
    	print(text)

    	# for phoneNumber in my_phone_numbers:

	    # 	client.messages.create(
	    #         from_=my_twilio_number,
	    #         to=phoneNumber,
	    #         body=text)
    else:
    	print "No new locker codes"
    	

if __name__ == '__main__':

    send_lockercode_sms()




